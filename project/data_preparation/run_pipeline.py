"""
run_pipeline.py
---------------
Main runner สำหรับ Data Preparation Pipeline ทั้งหมด
รัน OCR + Text Extraction + Validation ในลำดับที่ถูกต้อง

การใช้งาน:
    python run_pipeline.py                    # รันทั้งหมด
    python run_pipeline.py --step ocr         # รันแค่ OCR
    python run_pipeline.py --step extract     # รันแค่ Text Extraction
    python run_pipeline.py --step validate    # รันแค่ Validation
    python run_pipeline.py --force-reprocess  # บังคับทำใหม่ทั้งหมด
"""

import argparse
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("pipeline.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# Pipeline Steps
# ─────────────────────────────────────────────────────────────────────────────


def step_ocr(force_reprocess: bool = False, verbose: bool = False) -> bool:
    """
    Step 1: OCR สำหรับ Image PDFs (2475–2502)
    """
    logger.info("\n" + "━" * 60)
    logger.info("STEP 1: OCR Pipeline (Image PDFs: 2475–2502)")
    logger.info("━" * 60)

    try:
        from ocr_pipeline_01 import run_ocr_pipeline  # type: ignore
    except ImportError:
        # ถ้า import ไม่ได้ ให้รันเป็น subprocess แทน
        import subprocess

        cmd = [sys.executable, "01_ocr_pipeline.py"]
        if force_reprocess:
            cmd.append("--force-reprocess")
        if verbose:
            cmd.append("--verbose")
        result = subprocess.run(cmd, cwd=Path(__file__).parent)
        return result.returncode == 0

    try:
        run_ocr_pipeline(force_reprocess=force_reprocess)
        return True
    except Exception as e:
        logger.error(f"OCR Pipeline ล้มเหลว: {e}")
        return False


def step_extract(force_reprocess: bool = False, verbose: bool = False) -> bool:
    """
    Step 2: Text Extraction สำหรับ Text PDFs (2511–2564)
    """
    logger.info("\n" + "━" * 60)
    logger.info("STEP 2: Text Extraction Pipeline (Text PDFs: 2511–2564)")
    logger.info("━" * 60)

    import subprocess

    cmd = [sys.executable, "02_text_extraction.py"]
    if not force_reprocess:
        cmd.append("--skip-existing")
    if verbose:
        cmd.append("--verbose")
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    return result.returncode == 0


def step_validate(verbose: bool = False) -> bool:
    """
    Step 3: Validation & QA Report
    """
    logger.info("\n" + "━" * 60)
    logger.info("STEP 3: Validation & QA Report")
    logger.info("━" * 60)

    import subprocess

    cmd = [sys.executable, "03_validate_output.py"]
    if verbose:
        cmd.append("--verbose")
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    return result.returncode == 0


def step_merge_outputs() -> bool:
    """
    Step 4 (Optional): รวม JSON ทั้งหมดเป็นไฟล์เดียว
    """
    logger.info("\n" + "━" * 60)
    logger.info("STEP 4: Merge Outputs")
    logger.info("━" * 60)

    try:
        import json

        import pandas as pd
        from config import CONSTITUTIONS, PROCESSED_DIR

        all_data = []
        json_files = sorted(PROCESSED_DIR.glob("const_*.json"))

        for json_file in json_files:
            with open(json_file, encoding="utf-8") as f:
                data = json.load(f)

            # สร้าง record สำหรับ DataFrame
            record = {
                "id": data["id"],
                "year_th": data["year_th"],
                "year_ce": data["year_ce"],
                "name_th": data["name_th"],
                "name_short": data["name_short"],
                "date_announced": data["date_announced"],
                "source_type": data["source_type"],
                "processing_method": data["processing_method"],
                "era": data["era"],
                "regime_type": data["regime_type"],
                "total_pages": data.get("total_pages", len(data.get("pages", []))),
                "total_chars": data["metadata"]["total_chars"],
                "total_words_approx": data["metadata"]["total_words_approx"],
                "full_text": data["full_text"],
                "notes": data.get("notes", ""),
            }
            all_data.append(record)

        if not all_data:
            logger.warning("ไม่พบไฟล์ JSON ผลลัพธ์")
            return False

        # บันทึก combined JSON
        combined_path = PROCESSED_DIR / "all_constitutions.json"
        with open(combined_path, "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        logger.info(f"บันทึก combined JSON ที่ {combined_path}")

        # บันทึก CSV (ไม่รวม full_text เพื่อให้ไฟล์ไม่ใหญ่เกิน)
        df = pd.DataFrame(all_data)
        csv_cols = [c for c in df.columns if c != "full_text"]
        csv_path = PROCESSED_DIR / "all_constitutions.csv"
        df[csv_cols].to_csv(csv_path, index=False, encoding="utf-8-sig")
        logger.info(f"บันทึก combined CSV ที่ {csv_path}")

        # บันทึก plain text ต่อฉบับ
        txt_dir = PROCESSED_DIR / "plain_texts"
        txt_dir.mkdir(exist_ok=True)
        for record in all_data:
            txt_path = txt_dir / f"{record['id']}.txt"
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(record["full_text"])
        logger.info(f"บันทึก plain texts ที่ {txt_dir}/")

        logger.info(f"\nรวม {len(all_data)} ฉบับ เสร็จสิ้น")
        return True

    except Exception as e:
        logger.error(f"Merge ล้มเหลว: {e}")
        return False


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Data Preparation Pipeline — Thai Constitution Analysis (CPE232)"
    )
    parser.add_argument(
        "--step",
        choices=["ocr", "extract", "validate", "merge", "all"],
        default="all",
        help="ขั้นตอนที่ต้องการรัน (default: all)",
    )
    parser.add_argument(
        "--force-reprocess",
        action="store_true",
        help="บังคับทำใหม่แม้ทำไปแล้ว",
    )
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    start_time = time.time()

    logger.info("=" * 60)
    logger.info("DATA PREPARATION PIPELINE")
    logger.info("Thai Constitution Analysis — CPE232")
    logger.info(f"เริ่มต้น: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 60)

    success = True

    if args.step in ("ocr", "all"):
        ok = step_ocr(force_reprocess=args.force_reprocess, verbose=args.verbose)
        if not ok:
            logger.error("OCR step ล้มเหลว")
            success = False

    if args.step in ("extract", "all"):
        ok = step_extract(force_reprocess=args.force_reprocess, verbose=args.verbose)
        if not ok:
            logger.error("Extract step ล้มเหลว")
            success = False

    if args.step in ("validate", "all"):
        ok = step_validate(verbose=args.verbose)
        if not ok:
            logger.warning("Validate step มีปัญหา (ดู QA report)")

    if args.step in ("merge", "all"):
        ok = step_merge_outputs()
        if not ok:
            logger.warning("Merge step ล้มเหลว")

    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)

    logger.info("\n" + "=" * 60)
    logger.info(f"Pipeline {'เสร็จสิ้น ✅' if success else 'มีข้อผิดพลาด ❌'}")
    logger.info(f"เวลาที่ใช้: {minutes} นาที {seconds} วินาที")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
