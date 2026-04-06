"""
01_ocr_pipeline.py
------------------
OCR Pipeline สำหรับรัฐธรรมนูญไทยในรูปแบบ Image PDF (พ.ศ. 2475–2502)
ใช้ Typhoon OCR 1.5 ผ่าน API ของ OpenTyphoon.ai

การใช้งาน:
    python 01_ocr_pipeline.py                          # ประมวลผลทั้งหมด
    python 01_ocr_pipeline.py --ids const_2475         # เลือกเฉพาะบางฉบับ
    python 01_ocr_pipeline.py --skip-existing          # ข้ามที่ทำไปแล้ว
    python 01_ocr_pipeline.py --force-reprocess        # บังคับทำใหม่

ต้องการ:
    - TYPHOON_OCR_API_KEY ใน .env หรือ environment variable
    - ไฟล์ PDF วางใน data/raw_pdfs/
"""

import argparse
import json
import logging
import os
import time
from datetime import datetime
from pathlib import Path

# โหลด config จาก config.py
from config import (
    OCR_OUTPUT_DIR,
    PROCESSED_DIR,
    RAW_PDF_DIR,
    get_constitution_by_id,
    get_image_pdfs,
)
from dotenv import load_dotenv
from tenacity import before_sleep_log, retry, stop_after_attempt, wait_exponential
from tqdm import tqdm

# ─────────────────────────────────────────────────────────────────────────────
# Setup
# ─────────────────────────────────────────────────────────────────────────────
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("ocr_pipeline.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)

# Rate Limit: Typhoon OCR API — 2 req/s, 20 req/min
MIN_INTERVAL_BETWEEN_REQUESTS = 3.0  # วินาที (เผื่อ margin)
MAX_PAGES_PER_MINUTE = 18  # conservative (< 20 req/min)


# ─────────────────────────────────────────────────────────────────────────────
# OCR Function (with retry logic)
# ─────────────────────────────────────────────────────────────────────────────
@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=60),
    before_sleep=before_sleep_log(logger, logging.WARNING),
)
def ocr_single_page(pdf_path: Path, page_num: int) -> str:
    """
    ทำ OCR หน้าเดียวของ PDF ด้วย Typhoon OCR 1.5

    Args:
        pdf_path: Path ของไฟล์ PDF
        page_num: หมายเลขหน้า (เริ่มที่ 1)

    Returns:
        str: ผลลัพธ์ OCR ในรูปแบบ Markdown
    """
    from typhoon_ocr import ocr_document  # import ที่นี่เพื่อให้ retry ทำงานได้ถูกต้อง

    markdown = ocr_document(
        pdf_or_image_path=str(pdf_path),
        page_num=page_num,
    )
    return markdown


# ─────────────────────────────────────────────────────────────────────────────
# PDF Page Count
# ─────────────────────────────────────────────────────────────────────────────
def get_pdf_page_count(pdf_path: Path) -> int:
    """
    นับจำนวนหน้าใน PDF

    Args:
        pdf_path: Path ของไฟล์ PDF

    Returns:
        int: จำนวนหน้าทั้งหมด
    """
    try:
        import fitz  # PyMuPDF

        doc = fitz.open(str(pdf_path))
        count = len(doc)
        doc.close()
        return count
    except Exception as e:
        logger.error(f"ไม่สามารถนับหน้า PDF {pdf_path.name}: {e}")
        return 0


# ─────────────────────────────────────────────────────────────────────────────
# Process Single Constitution
# ─────────────────────────────────────────────────────────────────────────────
def process_constitution(
    metadata: dict,
    skip_existing: bool = True,
    force_reprocess: bool = False,
) -> dict | None:
    """
    ประมวลผล OCR รัฐธรรมนูญ 1 ฉบับ

    Args:
        metadata:        ข้อมูล metadata จาก config.py
        skip_existing:   ข้ามถ้าทำเสร็จแล้ว
        force_reprocess: บังคับทำใหม่แม้ทำไปแล้ว

    Returns:
        dict: ผลลัพธ์ที่พร้อมบันทึก หรือ None ถ้าข้าม
    """
    const_id = metadata["id"]
    pdf_path = RAW_PDF_DIR / metadata["filename"]
    cache_dir = OCR_OUTPUT_DIR / const_id
    out_path = PROCESSED_DIR / f"{const_id}.json"

    # ─── ตรวจสอบว่าไฟล์ PDF มีอยู่ ───
    if not pdf_path.exists():
        logger.warning(f"[{const_id}] ไม่พบไฟล์ PDF: {pdf_path}")
        logger.warning(f"  กรุณาดาวน์โหลดจาก: {metadata['source_url']}")
        return None

    # ─── ตรวจสอบว่าทำไปแล้ว ───
    if out_path.exists() and skip_existing and not force_reprocess:
        logger.info(f"[{const_id}] ข้ามเพราะทำเสร็จแล้ว (ใช้ --force-reprocess เพื่อทำใหม่)")
        with open(out_path, encoding="utf-8") as f:
            return json.load(f)

    # ─── สร้าง cache directory ───
    cache_dir.mkdir(parents=True, exist_ok=True)

    # ─── นับหน้า ───
    total_pages = get_pdf_page_count(pdf_path)
    if total_pages == 0:
        logger.error(f"[{const_id}] ไม่สามารถนับหน้าได้")
        return None

    logger.info(f"[{const_id}] เริ่มทำ OCR — {metadata['name_th']}")
    logger.info(f"  ไฟล์ : {pdf_path.name}")
    logger.info(f"  หน้า : {total_pages} หน้า")
    logger.info(
        f"  เวลาประมาณ: ~{int(total_pages * MIN_INTERVAL_BETWEEN_REQUESTS / 60)} นาที"
    )

    pages_data = []
    last_request_at = 0.0

    # ─── OCR ทีละหน้า ───
    for page_num in tqdm(
        range(1, total_pages + 1), desc=f"OCR {const_id}", unit="page"
    ):
        cache_file = cache_dir / f"page_{page_num:03d}.md"

        # ── ใช้ cache ถ้ามี ──
        if cache_file.exists() and not force_reprocess:
            with open(cache_file, encoding="utf-8") as f:
                raw_markdown = f.read()
            logger.debug(f"  [หน้า {page_num}] ใช้ cache")
        else:
            # ── Rate limiting ──
            elapsed = time.time() - last_request_at
            if elapsed < MIN_INTERVAL_BETWEEN_REQUESTS:
                time.sleep(MIN_INTERVAL_BETWEEN_REQUESTS - elapsed)

            try:
                raw_markdown = ocr_single_page(pdf_path, page_num)
                last_request_at = time.time()

                # บันทึก cache
                with open(cache_file, "w", encoding="utf-8") as f:
                    f.write(raw_markdown)
                logger.debug(
                    f"  [หน้า {page_num}] OCR สำเร็จ ({len(raw_markdown)} ตัวอักษร)"
                )

            except Exception as e:
                logger.error(f"  [หน้า {page_num}] OCR ล้มเหลว: {e}")
                raw_markdown = ""

        has_figure = "<figure>" in raw_markdown.lower()

        pages_data.append(
            {
                "page_num": page_num,
                "raw_markdown": raw_markdown,
                "has_figure": has_figure,
                "char_count": len(raw_markdown),
            }
        )

    # ─── รวมข้อความทั้งหมด ───
    full_text = _combine_pages_to_text(pages_data)

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
        "processing_method": "typhoon-ocr-1.5",
        "processed_at": datetime.now().isoformat(),
        "total_pages": total_pages,
        "era": metadata["era"],
        "regime_type": metadata["regime_type"],
        "notes": metadata.get("notes"),
        "pages": pages_data,
        "full_text": full_text,
        "metadata": {
            "total_chars": len(full_text),
            "total_words_approx": len(full_text.split()),
            "pages_with_figures": sum(1 for p in pages_data if p["has_figure"]),
        },
    }

    # ─── บันทึก JSON ───
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    logger.info(f"[{const_id}] เสร็จสิ้น — บันทึกที่ {out_path}")
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Text Combination Helpers
# ─────────────────────────────────────────────────────────────────────────────
def _combine_pages_to_text(pages_data: list[dict]) -> str:
    """
    รวม Markdown จากทุกหน้าเป็น plain text เดียว
    - ลบ HTML tags ที่ไม่จำเป็น
    - รวม page breaks อย่างเหมาะสม
    """
    import re

    combined_parts = []
    for page in pages_data:
        text = page["raw_markdown"]
        if not text.strip():
            continue

        # ลบ page_number tag
        text = re.sub(r"<page_number>.*?</page_number>", "", text, flags=re.DOTALL)
        # ลบ figure description (เก็บไว้ใน pages_data แล้ว)
        text = re.sub(r"<figure>.*?</figure>", "[รูปภาพ]", text, flags=re.DOTALL)
        # Normalize whitespace
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = text.strip()

        if text:
            combined_parts.append(text)

    return "\n\n---\n\n".join(combined_parts)


# ─────────────────────────────────────────────────────────────────────────────
# Main Pipeline
# ─────────────────────────────────────────────────────────────────────────────
def run_ocr_pipeline(
    target_ids: list[str] | None = None,
    skip_existing: bool = True,
    force_reprocess: bool = False,
) -> None:
    """
    รัน OCR Pipeline สำหรับรัฐธรรมนูญ Image PDF ทั้งหมด (หรือที่เลือก)

    Args:
        target_ids:      list ของ ID ที่ต้องการประมวลผล (None = ทั้งหมด)
        skip_existing:   ข้ามไฟล์ที่ทำไปแล้ว
        force_reprocess: บังคับทำใหม่
    """
    # ตรวจสอบ API Key
    api_key = os.getenv("TYPHOON_OCR_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "ไม่พบ API Key!\n"
            "กรุณาตั้งค่า TYPHOON_OCR_API_KEY ใน .env หรือ environment variable\n"
            "สมัครที่: https://opentyphoon.ai"
        )

    image_pdfs = get_image_pdfs()

    # กรองเฉพาะ ID ที่ต้องการ
    if target_ids:
        image_pdfs = [c for c in image_pdfs if c["id"] in target_ids]
        missing = set(target_ids) - {c["id"] for c in image_pdfs}
        if missing:
            logger.warning(f"ไม่พบ ID เหล่านี้ใน image PDFs: {missing}")

    logger.info("=" * 60)
    logger.info("OCR PIPELINE — Thai Constitution Project")
    logger.info("=" * 60)
    logger.info(f"จำนวนเอกสารที่จะประมวลผล: {len(image_pdfs)} ฉบับ")
    logger.info(f"skip_existing   : {skip_existing}")
    logger.info(f"force_reprocess : {force_reprocess}")
    logger.info("=" * 60)

    results = []
    succeeded = 0
    failed = 0
    skipped = 0

    for i, metadata in enumerate(image_pdfs, 1):
        logger.info(f"\n[{i}/{len(image_pdfs)}] กำลังประมวลผล: {metadata['id']}")
        try:
            result = process_constitution(
                metadata,
                skip_existing=skip_existing,
                force_reprocess=force_reprocess,
            )
            if result is not None:
                results.append(result)
                succeeded += 1
            else:
                skipped += 1
        except Exception as e:
            logger.error(f"  ข้อผิดพลาดร้ายแรง: {e}")
            failed += 1

    logger.info("\n" + "=" * 60)
    logger.info("สรุปผลการทำ OCR")
    logger.info("=" * 60)
    logger.info(f"  สำเร็จ : {succeeded}")
    logger.info(f"  ข้าม   : {skipped}")
    logger.info(f"  ล้มเหลว: {failed}")
    logger.info("=" * 60)

    # บันทึก summary
    _save_summary(results, pipeline_type="ocr")


def _save_summary(results: list[dict], pipeline_type: str) -> None:
    """บันทึก summary ของผลลัพธ์ทั้งหมดเป็น CSV"""
    if not results:
        return

    import csv

    summary_path = PROCESSED_DIR / f"summary_{pipeline_type}.csv"
    fieldnames = [
        "id",
        "year_th",
        "year_ce",
        "name_short",
        "source_type",
        "total_pages",
        "total_chars",
        "total_words_approx",
        "pages_with_figures",
        "era",
        "regime_type",
        "processed_at",
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
                "total_pages": r.get("total_pages", r.get("total_pages", 0)),
                "total_chars": r["metadata"].get("total_chars", 0),
                "total_words_approx": r["metadata"].get("total_words_approx", 0),
                "pages_with_figures": r["metadata"].get("pages_with_figures", 0),
                "era": r["era"],
                "regime_type": r["regime_type"],
                "processed_at": r.get("processed_at", ""),
            }
            writer.writerow(row)

    logger.info(f"บันทึก summary ที่ {summary_path}")


# ─────────────────────────────────────────────────────────────────────────────
# CLI Entry Point
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="OCR Pipeline สำหรับรัฐธรรมนูญไทย Image PDFs (2475–2502)"
    )
    parser.add_argument(
        "--ids",
        nargs="+",
        help="ID ของรัฐธรรมนูญที่ต้องการประมวลผล เช่น const_2475 const_2492",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="ข้ามไฟล์ที่ประมวลผลไปแล้ว (default: True)",
    )
    parser.add_argument(
        "--force-reprocess",
        action="store_true",
        default=False,
        help="บังคับประมวลผลใหม่แม้ทำไปแล้ว",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="แสดงข้อมูล debug เพิ่มเติม",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    run_ocr_pipeline(
        target_ids=args.ids,
        skip_existing=args.skip_existing,
        force_reprocess=args.force_reprocess,
    )
