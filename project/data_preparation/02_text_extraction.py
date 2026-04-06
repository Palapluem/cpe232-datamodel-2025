"""
02_text_extraction.py
----------------------
Text Extraction Pipeline สำหรับรัฐธรรมนูญไทยในรูปแบบ Text PDF (พ.ศ. 2511–2564)
ใช้ PyMuPDF (fitz) เป็นหลัก และ pdfplumber เป็น fallback

การใช้งาน:
    python 02_text_extraction.py                          # ประมวลผลทั้งหมด
    python 02_text_extraction.py --ids const_2540         # เลือกเฉพาะบางฉบับ
    python 02_text_extraction.py --skip-existing          # ข้ามที่ทำไปแล้ว
    python 02_text_extraction.py --method pymupdf         # เลือก method (pymupdf/pdfplumber)
"""

import argparse
import json
import logging
import re
import unicodedata
from datetime import datetime
from pathlib import Path

from config import (
    PROCESSED_DIR,
    RAW_PDF_DIR,
    TEXT_OUTPUT_DIR,
    get_text_pdfs,
)
from tqdm import tqdm

# ─────────────────────────────────────────────────────────────────────────────
# Setup
# ─────────────────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("text_extraction.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# Extraction Methods
# ─────────────────────────────────────────────────────────────────────────────
def extract_with_pymupdf(pdf_path: Path) -> list[dict]:
    """
    ดึงข้อความจาก PDF ด้วย PyMuPDF (fitz)
    เหมาะสำหรับ PDF ที่มีข้อความแบบ selectable

    Args:
        pdf_path: Path ของไฟล์ PDF

    Returns:
        list[dict]: ข้อมูลแต่ละหน้า
    """
    import fitz  # PyMuPDF

    doc = fitz.open(str(pdf_path))
    pages = []

    for page_idx in range(len(doc)):
        page = doc[page_idx]
        page_num = page_idx + 1
        text = page.get_text("text")  # รูปแบบ plain text

        # ลอง blocks mode ถ้า plain text ได้น้อย
        if len(text.strip()) < 100:
            blocks = page.get_text("blocks")
            text = "\n".join(b[4] for b in blocks if isinstance(b[4], str))

        pages.append(
            {
                "page_num": page_num,
                "raw_text": text,
                "char_count": len(text),
            }
        )

    doc.close()
    return pages


def extract_with_pdfplumber(pdf_path: Path) -> list[dict]:
    """
    ดึงข้อความจาก PDF ด้วย pdfplumber
    มีประสิทธิภาพดีกับ PDF ที่มี layout ซับซ้อน

    Args:
        pdf_path: Path ของไฟล์ PDF

    Returns:
        list[dict]: ข้อมูลแต่ละหน้า
    """
    import pdfplumber

    pages = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page_idx, page in enumerate(pdf.pages):
            page_num = page_idx + 1
            text = (
                page.extract_text(
                    x_tolerance=3,
                    y_tolerance=3,
                    layout=True,
                )
                or ""
            )

            pages.append(
                {
                    "page_num": page_num,
                    "raw_text": text,
                    "char_count": len(text),
                }
            )

    return pages


def smart_extract(pdf_path: Path) -> tuple[list[dict], str]:
    """
    เลือก method การดึงข้อความอัตโนมัติ
    ลอง PyMuPDF ก่อน ถ้าได้ข้อมูลน้อยเกินไปให้สลับไป pdfplumber

    Returns:
        (pages_data, method_used)
    """
    # ลอง PyMuPDF ก่อน
    try:
        pages = extract_with_pymupdf(pdf_path)
        total_chars = sum(p["char_count"] for p in pages)

        if total_chars > 500:  # ถ้าได้ข้อมูลพอ
            logger.debug(f"  ใช้ PyMuPDF ({total_chars} ตัวอักษร)")
            return pages, "pymupdf"
        else:
            logger.debug(f"  PyMuPDF ได้ข้อมูลน้อย ({total_chars} ตัวอักษร) สลับไป pdfplumber")
    except Exception as e:
        logger.warning(f"  PyMuPDF ล้มเหลว: {e}")

    # Fallback: pdfplumber
    try:
        pages = extract_with_pdfplumber(pdf_path)
        logger.debug(f"  ใช้ pdfplumber")
        return pages, "pdfplumber"
    except Exception as e:
        logger.error(f"  pdfplumber ล้มเหลว: {e}")
        return [], "failed"


# ─────────────────────────────────────────────────────────────────────────────
# Text Post-Processing
# ─────────────────────────────────────────────────────────────────────────────
def normalize_thai_text(text: str) -> str:
    """
    Normalize ข้อความภาษาไทย:
    1. NFC Unicode normalization
    2. ลบ control characters
    3. Normalize spaces
    4. แปลงเลขไทย → เลขอารบิก
    5. Normalize Thai punctuation

    Args:
        text: ข้อความดิบ

    Returns:
        str: ข้อความที่ normalize แล้ว
    """
    if not text:
        return ""

    # 1. NFC Unicode normalization
    text = unicodedata.normalize("NFC", text)

    # 2. ลบ control characters (ยกเว้น newline และ tab)
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]", "", text)

    # 3. Normalize Thai digits → Arabic digits
    thai_digits = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")
    text = text.translate(thai_digits)

    # 4. Normalize spaces (รวม multiple spaces เป็น 1)
    text = re.sub(r"[ \t]+", " ", text)

    # 5. Normalize multiple newlines (รวม blank lines เกิน 2 บรรทัด)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 6. ลบ trailing whitespace ต่อบรรทัด
    lines = [line.rstrip() for line in text.split("\n")]
    text = "\n".join(lines)

    return text.strip()


def remove_header_footer(text: str) -> str:
    """
    ลบ Header/Footer ของราชกิจจานุเบกษาที่ปรากฏในทุกหน้า
    เช่น "หน้า X เล่ม X ตอนที่ X ราชกิจจานุเบกษา"

    Args:
        text: ข้อความที่มี header/footer

    Returns:
        str: ข้อความที่ลบ header/footer แล้ว
    """
    patterns = [
        # รูปแบบ header/footer ราชกิจจานุเบกษา
        r"หน้า\s*\d+\s*เล่ม\s*\d+.*?ราชกิจจานุเบกษา.*?\n",
        r"ราชกิจจานุเบกษา.*?เล่ม\s*\d+.*?หน้า\s*\d+.*?\n",
        r"เล่ม\s*\d+\s*ตอนที่\s*\d+\s*ก?.*?ราชกิจจานุเบกษา.*?\n",
        r"^\s*-\s*\d+\s*-\s*$",  # เลขหน้ากลางหน้า
        r"^\s*\d+\s*$",  # เลขหน้าเพียงอย่างเดียว (บรรทัดเดี่ยว)
    ]

    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE | re.IGNORECASE)

    return text.strip()


def clean_extracted_text(text: str) -> str:
    """รวม normalize + remove header/footer"""
    text = remove_header_footer(text)
    text = normalize_thai_text(text)
    return text


def combine_pages_text(pages_data: list[dict]) -> str:
    """รวมข้อความจากทุกหน้าเป็นข้อความเดียว"""
    parts = []
    for page in pages_data:
        text = page.get("cleaned_text") or page.get("raw_text", "")
        if text.strip():
            parts.append(text.strip())
    return "\n\n".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
# Process Single Constitution
# ─────────────────────────────────────────────────────────────────────────────
def process_constitution(
    metadata: dict,
    skip_existing: bool = True,
    method: str = "smart",
) -> dict | None:
    """
    ดึงข้อความจากรัฐธรรมนูญ Text PDF 1 ฉบับ

    Args:
        metadata:      ข้อมูล metadata จาก config.py
        skip_existing: ข้ามถ้าทำเสร็จแล้ว
        method:        "smart" | "pymupdf" | "pdfplumber"

    Returns:
        dict: ผลลัพธ์ที่พร้อมบันทึก หรือ None ถ้าข้าม/ล้มเหลว
    """
    const_id = metadata["id"]
    pdf_path = RAW_PDF_DIR / metadata["filename"]
    out_path = PROCESSED_DIR / f"{const_id}.json"

    # ─── ตรวจสอบว่าไฟล์ PDF มีอยู่ ───
    if not pdf_path.exists():
        logger.warning(f"[{const_id}] ไม่พบไฟล์ PDF: {pdf_path}")
        logger.warning(f"  กรุณาดาวน์โหลดจาก: {metadata['source_url']}")
        return None

    # ─── ตรวจสอบว่าทำไปแล้ว ───
    if out_path.exists() and skip_existing:
        logger.info(f"[{const_id}] ข้ามเพราะทำเสร็จแล้ว")
        with open(out_path, encoding="utf-8") as f:
            return json.load(f)

    logger.info(f"[{const_id}] เริ่มดึงข้อความ — {metadata['name_th']}")

    # ─── ดึงข้อความ ───
    if method == "smart":
        pages_data, method_used = smart_extract(pdf_path)
    elif method == "pymupdf":
        pages_data = extract_with_pymupdf(pdf_path)
        method_used = "pymupdf"
    elif method == "pdfplumber":
        pages_data = extract_with_pdfplumber(pdf_path)
        method_used = "pdfplumber"
    else:
        raise ValueError(f"method ไม่ถูกต้อง: {method}")

    if not pages_data:
        logger.error(f"[{const_id}] ไม่สามารถดึงข้อความได้")
        return None

    # ─── Post-processing แต่ละหน้า ───
    for page in pages_data:
        page["cleaned_text"] = clean_extracted_text(page["raw_text"])

    # ─── รวมข้อความทั้งหมด ───
    full_text = combine_pages_text(pages_data)
    full_text_norm = normalize_thai_text(full_text)

    # ─── สร้าง output JSON ───
    result = {
        "id": const_id,
        "year_th": metadata["year_th"],
        "year_ce": metadata["year_ce"],
        "name_th": metadata["name_th"],
        "name_short": metadata["name_short"],
        "date_announced": metadata["date_announced"],
        "source_url": metadata["source_url"],
        "source_type": metadata["source_type"],
        "processing_method": method_used,
        "processed_at": datetime.now().isoformat(),
        "total_pages": len(pages_data),
        "era": metadata["era"],
        "regime_type": metadata["regime_type"],
        "notes": metadata.get("notes"),
        "pages": pages_data,
        "full_text": full_text_norm,
        "metadata": {
            "total_chars": len(full_text_norm),
            "total_words_approx": len(full_text_norm.split()),
            "empty_pages": sum(1 for p in pages_data if not p["cleaned_text"].strip()),
        },
    }

    # ─── บันทึก JSON ───
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    total_chars = result["metadata"]["total_chars"]
    logger.info(f"[{const_id}] เสร็จสิ้น — {len(pages_data)} หน้า, {total_chars:,} ตัวอักษร")
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Main Pipeline
# ─────────────────────────────────────────────────────────────────────────────
def run_text_extraction_pipeline(
    target_ids: list[str] | None = None,
    skip_existing: bool = True,
    method: str = "smart",
) -> None:
    """
    รัน Text Extraction Pipeline สำหรับรัฐธรรมนูญ Text PDF ทั้งหมด

    Args:
        target_ids:    list ของ ID ที่ต้องการ (None = ทั้งหมด)
        skip_existing: ข้ามไฟล์ที่ทำไปแล้ว
        method:        extraction method
    """
    text_pdfs = get_text_pdfs()

    if target_ids:
        text_pdfs = [c for c in text_pdfs if c["id"] in target_ids]

    logger.info("=" * 60)
    logger.info("TEXT EXTRACTION PIPELINE — Thai Constitution Project")
    logger.info("=" * 60)
    logger.info(f"จำนวนเอกสารที่จะประมวลผล: {len(text_pdfs)} ฉบับ")
    logger.info(f"Method: {method}")
    logger.info("=" * 60)

    results = []
    succeeded = 0
    failed = 0
    skipped = 0

    for i, metadata in enumerate(
        tqdm(text_pdfs, desc="Text Extraction", unit="file"), 1
    ):
        logger.info(f"\n[{i}/{len(text_pdfs)}] {metadata['id']}")
        try:
            result = process_constitution(metadata, skip_existing, method)
            if result is not None:
                results.append(result)
                succeeded += 1
            else:
                skipped += 1
        except Exception as e:
            logger.error(f"  ข้อผิดพลาด: {e}")
            failed += 1

    logger.info("\n" + "=" * 60)
    logger.info("สรุปผล Text Extraction")
    logger.info("=" * 60)
    logger.info(f"  สำเร็จ : {succeeded}")
    logger.info(f"  ข้าม   : {skipped}")
    logger.info(f"  ล้มเหลว: {failed}")

    # บันทึก summary CSV
    _save_summary(results)


def _save_summary(results: list[dict]) -> None:
    """บันทึก summary CSV"""
    if not results:
        return

    import csv

    summary_path = PROCESSED_DIR / "summary_text_extraction.csv"
    fieldnames = [
        "id",
        "year_th",
        "year_ce",
        "name_short",
        "source_type",
        "processing_method",
        "total_pages",
        "total_chars",
        "total_words_approx",
        "empty_pages",
        "era",
        "regime_type",
    ]

    with open(summary_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            row = {
                "id": r["id"],
                "year_th": r["year_th"],
                "year_ce": r["year_ce"],
                "name_short": r["name_short"],
                "source_type": r["source_type"],
                "processing_method": r["processing_method"],
                "total_pages": r["total_pages"],
                "total_chars": r["metadata"]["total_chars"],
                "total_words_approx": r["metadata"]["total_words_approx"],
                "empty_pages": r["metadata"]["empty_pages"],
                "era": r["era"],
                "regime_type": r["regime_type"],
            }
            writer.writerow(row)

    logger.info(f"บันทึก summary ที่ {summary_path}")


# ─────────────────────────────────────────────────────────────────────────────
# CLI Entry Point
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Text Extraction Pipeline สำหรับรัฐธรรมนูญไทย Text PDFs (2511–2564)"
    )
    parser.add_argument(
        "--ids",
        nargs="+",
        help="ID ของรัฐธรรมนูญที่ต้องการ เช่น const_2540 const_2560",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="ข้ามไฟล์ที่ทำไปแล้ว (default: True)",
    )
    parser.add_argument(
        "--method",
        choices=["smart", "pymupdf", "pdfplumber"],
        default="smart",
        help="Extraction method (default: smart)",
    )
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    run_text_extraction_pipeline(
        target_ids=args.ids,
        skip_existing=args.skip_existing,
        method=args.method,
    )
