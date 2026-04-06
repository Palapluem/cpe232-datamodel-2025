"""
03_validate_output.py
---------------------
ตรวจสอบคุณภาพผลลัพธ์จาก OCR Pipeline และ Text Extraction Pipeline
สร้าง QA Report สรุปคุณภาพข้อมูลของรัฐธรรมนูญแต่ละฉบับ

การใช้งาน:
    python 03_validate_output.py          # ตรวจสอบทั้งหมด
    python 03_validate_output.py --id const_2475  # ตรวจสอบฉบับเดียว
"""

import argparse
import json
import logging
import re
from datetime import datetime
from pathlib import Path

import pandas as pd
from config import CONSTITUTIONS, PROCESSED_DIR, get_constitution_by_id

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# Quality Check Rules
# ─────────────────────────────────────────────────────────────────────────────


class QualityChecker:
    """ตรวจสอบคุณภาพข้อความรัฐธรรมนูญ"""

    # OCR Error Patterns ที่พบบ่อยในภาษาไทย
    COMMON_OCR_ERRORS = [
        (r"[่้๊๋]{2,}", "วรรณยุกต์ซ้อนกัน"),
        (r"[^\u0000-\u007F\u0E00-\u0E7F\u0020-\u007E]{3,}", "ตัวอักษรแปลกปลอม"),
        (r"\d{5,}", "ตัวเลขยาวผิดปกติ"),
    ]

    # คำสำคัญที่ต้องมีในรัฐธรรมนูญ
    REQUIRED_KEYWORDS = [
        "มาตรา",
        "รัฐธรรมนูญ",
    ]

    # คำที่ไม่ควรมีมากในเอกสาร (OCR garbage)
    GARBAGE_INDICATORS = [
        r"[a-zA-Z]{20,}",  # อักษรอังกฤษยาวผิดปกติ (OCR artifact)
        r"[^\w\s\u0E00-\u0E7F]{5,}",  # สัญลักษณ์แปลกต่อเนื่อง
    ]

    def check(self, data: dict) -> dict:
        """
        ตรวจสอบคุณภาพ JSON ของรัฐธรรมนูญ 1 ฉบับ

        Returns:
            dict: ผลการตรวจสอบพร้อม score
        """
        issues = []
        warnings = []
        full_text = data.get("full_text", "")

        # ── 1. ตรวจสอบว่ามีข้อความ ──
        if not full_text.strip():
            issues.append("CRITICAL: full_text ว่างเปล่า")
        elif len(full_text) < 500:
            warnings.append(f"WARNING: full_text สั้นผิดปกติ ({len(full_text)} ตัวอักษร)")

        # ── 2. ตรวจสอบ required keywords ──
        for keyword in self.REQUIRED_KEYWORDS:
            if keyword not in full_text:
                warnings.append(f"WARNING: ไม่พบคำสำคัญ '{keyword}'")

        # ── 3. ตรวจสอบ OCR errors ──
        ocr_error_count = 0
        for pattern, desc in self.COMMON_OCR_ERRORS:
            matches = re.findall(pattern, full_text)
            if len(matches) > 10:
                ocr_error_count += len(matches)
                warnings.append(f"WARNING: พบ '{desc}' จำนวน {len(matches)} ครั้ง")

        # ── 4. ตรวจสอบ garbage characters ──
        for pattern in self.GARBAGE_INDICATORS:
            matches = re.findall(pattern, full_text)
            if matches:
                issues.append(
                    f"GARBAGE: พบรูปแบบ garbage '{pattern[:30]}' ({len(matches)} ครั้ง)"
                )

        # ── 5. ตรวจสอบ metadata ──
        required_fields = [
            "id",
            "year_th",
            "name_th",
            "source_type",
            "full_text",
            "pages",
        ]
        for field in required_fields:
            if field not in data:
                issues.append(f"MISSING_FIELD: ไม่มีฟิลด์ '{field}'")

        # ── 6. ตรวจสอบจำนวนหน้า ──
        pages = data.get("pages", [])
        if not pages:
            issues.append("CRITICAL: ไม่มีข้อมูลหน้า")
        else:
            empty_pages = sum(
                1
                for p in pages
                if not (p.get("raw_text") or p.get("raw_markdown") or "").strip()
            )
            if empty_pages > 0:
                pct = empty_pages / len(pages) * 100
                warnings.append(
                    f"WARNING: มีหน้าว่างเปล่า {empty_pages}/{len(pages)} หน้า ({pct:.1f}%)"
                )

        # ── 7. ตรวจสอบสัดส่วนอักษรไทย ──
        if full_text:
            thai_chars = len(re.findall(r"[\u0E00-\u0E7F]", full_text))
            total_chars = len(re.sub(r"\s", "", full_text))
            thai_ratio = thai_chars / total_chars if total_chars > 0 else 0

            if thai_ratio < 0.3:
                issues.append(
                    f"LOW_THAI_RATIO: อักษรไทยเพียง {thai_ratio:.1%} (ควรมากกว่า 30%)"
                )

        # ── คำนวณ Quality Score ──
        base_score = 100
        base_score -= len(issues) * 20  # หัก 20 ต่อ issue
        base_score -= len(warnings) * 5  # หัก 5 ต่อ warning
        quality_score = max(0, min(100, base_score))

        return {
            "id": data.get("id"),
            "quality_score": quality_score,
            "issues": issues,
            "warnings": warnings,
            "stats": {
                "char_count": len(full_text),
                "page_count": len(pages),
                "thai_ratio": round(thai_ratio if full_text else 0, 3),
                "ocr_errors": ocr_error_count,
            },
        }


# ─────────────────────────────────────────────────────────────────────────────
# Load & Validate All
# ─────────────────────────────────────────────────────────────────────────────


def validate_all(target_id: str | None = None) -> pd.DataFrame:
    """
    ตรวจสอบคุณภาพผลลัพธ์ทั้งหมด

    Args:
        target_id: ID ของรัฐธรรมนูญที่ต้องการ (None = ทั้งหมด)

    Returns:
        pd.DataFrame: ตารางสรุปคุณภาพ
    """
    checker = QualityChecker()
    results = []

    # ดึง JSON ที่ประมวลผลแล้วทั้งหมด
    json_files = sorted(PROCESSED_DIR.glob("const_*.json"))

    if target_id:
        json_files = [f for f in json_files if f.stem == target_id]

    if not json_files:
        logger.warning("ไม่พบไฟล์ผลลัพธ์ใน PROCESSED_DIR")
        logger.warning(f"Path: {PROCESSED_DIR}")
        return pd.DataFrame()

    logger.info(f"ตรวจสอบ {len(json_files)} ไฟล์...")

    for json_file in json_files:
        try:
            with open(json_file, encoding="utf-8") as f:
                data = json.load(f)

            qa_result = checker.check(data)

            # เพิ่ม metadata
            meta = get_constitution_by_id(data.get("id", "")) or {}
            qa_result.update(
                {
                    "year_th": data.get("year_th"),
                    "name_short": data.get("name_short", data.get("id")),
                    "source_type": data.get("source_type"),
                    "processing_method": data.get("processing_method"),
                    "era": data.get("era"),
                }
            )
            results.append(qa_result)

            # แสดงผล
            score_icon = (
                "✅"
                if qa_result["quality_score"] >= 80
                else "⚠️"
                if qa_result["quality_score"] >= 50
                else "❌"
            )
            logger.info(
                f"{score_icon} [{data.get('id')}] Score: {qa_result['quality_score']}/100 "
                f"| Issues: {len(qa_result['issues'])} "
                f"| Warnings: {len(qa_result['warnings'])}"
            )
            for issue in qa_result["issues"]:
                logger.error(f"    {issue}")
            for warning in qa_result["warnings"][:3]:  # แสดงแค่ 3 warning แรก
                logger.warning(f"    {warning}")

        except Exception as e:
            logger.error(f"ไม่สามารถตรวจสอบ {json_file.name}: {e}")

    if not results:
        return pd.DataFrame()

    df = pd.DataFrame(results)
    return df


def save_qa_report(df: pd.DataFrame) -> None:
    """บันทึก QA Report"""
    if df.empty:
        logger.warning("ไม่มีข้อมูลสำหรับบันทึก")
        return

    report_path = PROCESSED_DIR / "qa_report.csv"

    # เลือกเฉพาะ columns ที่เป็น scalar สำหรับ CSV
    scalar_cols = [
        "id",
        "year_th",
        "name_short",
        "source_type",
        "processing_method",
        "era",
        "quality_score",
    ]
    stats_cols = ["char_count", "page_count", "thai_ratio", "ocr_errors"]

    # Flatten stats dict
    for col in stats_cols:
        df[col] = df["stats"].apply(
            lambda x: x.get(col, 0) if isinstance(x, dict) else 0
        )

    issue_cols = scalar_cols + stats_cols
    export_df = df[[c for c in issue_cols if c in df.columns]].copy()
    export_df["issue_count"] = df["issues"].apply(len)
    export_df["warning_count"] = df["warnings"].apply(len)

    export_df.to_csv(report_path, index=False, encoding="utf-8-sig")
    logger.info(f"บันทึก QA Report ที่ {report_path}")

    # สรุปภาพรวม
    logger.info("\n" + "=" * 50)
    logger.info("QA SUMMARY")
    logger.info("=" * 50)
    logger.info(f"เอกสารทั้งหมด : {len(df)}")
    logger.info(f"Score เฉลี่ย  : {df['quality_score'].mean():.1f}/100")
    logger.info(f"Score >= 80   : {(df['quality_score'] >= 80).sum()} ฉบับ ✅")
    logger.info(
        f"Score 50–79   : {((df['quality_score'] >= 50) & (df['quality_score'] < 80)).sum()} ฉบับ ⚠️"
    )
    logger.info(f"Score < 50    : {(df['quality_score'] < 50).sum()} ฉบับ ❌")


# ─────────────────────────────────────────────────────────────────────────────
# CLI Entry Point
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ตรวจสอบคุณภาพผลลัพธ์จาก OCR และ Text Extraction Pipeline"
    )
    parser.add_argument(
        "--id",
        dest="target_id",
        help="ID ของรัฐธรรมนูญที่ต้องการตรวจสอบ เช่น const_2475",
    )
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    df = validate_all(target_id=args.target_id)
    save_qa_report(df)
