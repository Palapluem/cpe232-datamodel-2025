"""
config.py
---------
Configuration and metadata for all Thai Constitutions.
Covers 38 documents from พ.ศ. 2475 (1932) to พ.ศ. 2564 (2021).

Source: ระบบคลังสารสนเทศรัฐสภา
URL: https://catalog.parliament.go.th/dataset/12_01
"""

from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# Directory Paths
# ─────────────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
RAW_PDF_DIR = DATA_DIR / "raw_pdfs"
OCR_OUTPUT_DIR = DATA_DIR / "ocr_output"
TEXT_OUTPUT_DIR = DATA_DIR / "extracted_text"
PROCESSED_DIR = DATA_DIR / "processed"

# Ensure directories exist
for d in [RAW_PDF_DIR, OCR_OUTPUT_DIR, TEXT_OUTPUT_DIR, PROCESSED_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# Political Era Mapping
# ─────────────────────────────────────────────────────────────────────────────
ERA_LABELS = {
    "early_democracy": "ยุคประชาธิปไตยแรกเริ่ม (2475–2490)",
    "post_coup_1947": "ยุคหลังรัฐประหาร 2490 (2490–2502)",
    "dictatorship": "ยุคเผด็จการทหาร (2502–2516)",
    "democratic_spring": "ยุคประชาธิปไตย (2517–2519)",
    "semi_democracy": "ยุคกึ่งประชาธิปไตย (2520–2533)",
    "modern_democracy": "ยุคประชาธิปไตยสมัยใหม่ (2534–2549)",
    "post_coup_2006": "ยุคหลังรัฐประหาร 2549 (2549–2557)",
    "post_coup_2014": "ยุคหลังรัฐประหาร 2557 (2557–ปัจจุบัน)",
}

# ─────────────────────────────────────────────────────────────────────────────
# Constitution Metadata
# source_type: "image_pdf" → ต้องทำ OCR (ไฟล์ที่ 1–32)
#              "text_pdf"  → ดึงข้อความได้โดยตรง (ไฟล์ที่ 33–38)
# ─────────────────────────────────────────────────────────────────────────────
CONSTITUTIONS = [
    # ══════════════════════════════════════════════════════
    # IMAGE PDFs — ต้องทำ OCR ด้วย Typhoon OCR 1.5 (ไฟล์ที่ 1–32)
    # ══════════════════════════════════════════════════════
    {
        "id": "const_2475",
        "year_th": 2475,
        "year_ce": 1932,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรสยาม พ.ศ. 2475",
        "name_short": "รธน. 2475",
        "date_announced": "1932-12-10",
        "source_url": "https://hdl.handle.net/20.500.14156/290453",
        "source_type": "image_pdf",
        "filename": "01_รัฐธรรมนูญแห่งราชอาณาจักรสยาม พ.ศ. 2475.pdf",
        "era": "early_democracy",
        "regime_type": "civilian",
        "notes": "รัฐธรรมนูญฉบับแรกของไทย",
    },
    {
        "id": "const_2482",
        "year_th": 2482,
        "year_ce": 1939,
        "name_th": "รัฐธรรมนูญแก้ไขเพิ่มเติมว่าด้วยนามประเทศ พ.ศ. 2482",
        "name_short": "รธน. 2482",
        "date_announced": "1939-10-06",
        "source_url": "https://hdl.handle.net/20.500.14156/290417",
        "source_type": "image_pdf",
        "filename": "02_รัฐธรรมนูญแก้ไขเพิ่มเติมว่าด้วยนามประเทศ พ.ศ. 2482.pdf",
        "era": "early_democracy",
        "regime_type": "civilian",
        "notes": "แก้ไขชื่อประเทศจาก สยาม เป็น ไทย",
    },
    {
        "id": "const_2483",
        "year_th": 2483,
        "year_ce": 1940,
        "name_th": "รัฐธรรมนูญแก้ไขเพิ่มเติมว่าด้วยบทเฉพาะกาล พ.ศ. 2483",
        "name_short": "รธน. 2483",
        "date_announced": "1940-10-04",
        "source_url": "https://hdl.handle.net/20.500.14156/290418",
        "source_type": "image_pdf",
        "filename": "03_รัฐธรรมนูญแก้ไขเพิ่มเติมว่าด้วยบทเฉพาะกาล พ.ศ. 2483.pdf",
        "era": "early_democracy",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2485",
        "year_th": 2485,
        "year_ce": 1942,
        "name_th": "รัฐธรรมนูญแก้ไขเพิ่มเติมว่าด้วยการเลือกตั้งสมาชิกสภาผู้แทนราษฎร พุทธศักราช 2485",
        "name_short": "รธน. 2485",
        "date_announced": "1942-12-03",
        "source_url": "https://hdl.handle.net/20.500.14156/290419",
        "source_type": "image_pdf",
        "filename": "04_รัถธัมนูญแก้ไขเพิ่มเติมว่าด้วยการเลือกตั้งสมาชิกสภาผู้แทนราสดร พุทธสักราช 2485.pdf",
        "era": "early_democracy",
        "regime_type": "military",
        "notes": None,
    },
    {
        "id": "const_2489",
        "year_th": 2489,
        "year_ce": 1946,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2489",
        "name_short": "รธน. 2489",
        "date_announced": "1946-05-10",
        "source_url": "https://hdl.handle.net/20.500.14156/290420",
        "source_type": "image_pdf",
        "filename": "05_รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2489.pdf",
        "era": "early_democracy",
        "regime_type": "civilian",
        "notes": "ถูกยกเลิกโดยรัฐประหาร 2490",
    },
    {
        "id": "const_2490a",
        "year_th": 2490,
        "year_ce": 1947,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉะบับชั่วคราว) พ.ศ. 2490",
        "name_short": "รธน. 2490 (ชั่วคราว)",
        "date_announced": "1947-11-09",
        "source_url": "https://hdl.handle.net/20.500.14156/290421",
        "source_type": "image_pdf",
        "filename": "06_รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉะบับชั่วคราว) พ.ศ. 2490.pdf",
        "era": "post_coup_1947",
        "regime_type": "military",
        "notes": "หลังรัฐประหาร 8 พ.ย. 2490",
    },
    {
        "id": "const_2490b",
        "year_th": 2490,
        "year_ce": 1947,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉบับชั่วคราว) แก้ไขเพิ่มเติม พ.ศ. 2490",
        "name_short": "รธน. 2490 แก้ไข",
        "date_announced": "1947-12-09",
        "source_url": "https://hdl.handle.net/20.500.14156/290422",
        "source_type": "image_pdf",
        "filename": "07_รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉบับชั่วคราว) แก้ไขเพิ่มเติม พ.ศ. 2490.pdf",
        "era": "post_coup_1947",
        "regime_type": "military",
        "notes": None,
    },
    {
        "id": "const_2491a",
        "year_th": 2491,
        "year_ce": 1948,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉะบับชั่วคราว) แก้ไขเพิ่มเติม (ฉะบับที่ 2) พ.ศ. 2491",
        "name_short": "รธน. 2491 (ฉบับที่ 2)",
        "date_announced": "1948-02-03",
        "source_url": "https://hdl.handle.net/20.500.14156/290440",
        "source_type": "image_pdf",
        "filename": "08_รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉะบับชั่วคราว) แก้ไขเพิ่มเติม (ฉะบับที่ 2) พ.ศ. 2491.pdf",
        "era": "post_coup_1947",
        "regime_type": "military",
        "notes": None,
    },
    {
        "id": "const_2491b",
        "year_th": 2491,
        "year_ce": 1948,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉบับชั่วคราว) แก้ไขเพิ่มเติม (ฉบับที่ 3) พ.ศ. 2491",
        "name_short": "รธน. 2491 (ฉบับที่ 3)",
        "date_announced": "1948-08-24",
        "source_url": "https://hdl.handle.net/20.500.14156/290423",
        "source_type": "image_pdf",
        "filename": "09_รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉบับชั่วคราว) แก้ไขเพิ่มเติม (ฉบับที่ 3) พ.ศ. 2491.pdf",
        "era": "post_coup_1947",
        "regime_type": "military",
        "notes": None,
    },
    {
        "id": "const_2492",
        "year_th": 2492,
        "year_ce": 1949,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2492",
        "name_short": "รธน. 2492",
        "date_announced": "1949-03-23",
        "source_url": "https://hdl.handle.net/20.500.14156/290442",
        "source_type": "image_pdf",
        "filename": "10_รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2492.pdf",
        "era": "post_coup_1947",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2495",
        "year_th": 2495,
        "year_ce": 1952,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พุทธศักราช 2475 แก้ไขเพิ่มเติม พุทธศักราช 2495",
        "name_short": "รธน. 2495",
        "date_announced": "1952-03-08",
        "source_url": "https://hdl.handle.net/20.500.14156/290425",
        "source_type": "image_pdf",
        "filename": "11_รัฐธรรมนูญแห่งราชอาณาจักรไทย พุทธศักราช 2475 แก้ไขเพิ่มเติม พุทธศักราช 2495.pdf",
        "era": "post_coup_1947",
        "regime_type": "military",
        "notes": None,
    },
    {
        "id": "const_2502",
        "year_th": 2502,
        "year_ce": 1959,
        "name_th": "ธรรมนูญการปกครองราชอาณาจักร พุทธศักราช 2502",
        "name_short": "ธรรมนูญ 2502",
        "date_announced": "1959-01-28",
        "source_url": "https://hdl.handle.net/20.500.14156/290441",
        "source_type": "image_pdf",
        "filename": "12_ธรรมนูญการปกครองราชอาณาจักร พ.ศ. 2502.pdf",
        "era": "dictatorship",
        "regime_type": "military",
        "notes": "ยุคจอมพลสฤษดิ์ ธนะรัชต์",
    },
    # ══════════════════════════════════════════════════════
    # IMAGE PDFs (ต่อ) — ไฟล์ที่ 13–32 ยังเป็น Image PDF ต้องทำ OCR
    # ══════════════════════════════════════════════════════
    {
        "id": "const_2511",
        "year_th": 2511,
        "year_ce": 1968,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2511",
        "name_short": "รธน. 2511",
        "date_announced": "1968-06-20",
        "source_url": "https://hdl.handle.net/20.500.14156/290428",
        "source_type": "image_pdf",
        "filename": "13_รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2511.pdf",
        "era": "dictatorship",
        "regime_type": "military",
        "notes": None,
    },
    {
        "id": "const_2515",
        "year_th": 2515,
        "year_ce": 1972,
        "name_th": "ธรรมนูญการปกครองราชอาณาจักร พุทธศักราช 2515",
        "name_short": "ธรรมนูญ 2515",
        "date_announced": "1972-12-15",
        "source_url": "https://hdl.handle.net/20.500.14156/290429",
        "source_type": "image_pdf",
        "filename": "14_ธรรมนูญการปกครองราชอาณาจักร พุทธศักราช 2515.pdf",
        "era": "dictatorship",
        "regime_type": "military",
        "notes": "ยุคจอมพลถนอม กิตติขจร",
    },
    {
        "id": "const_2517",
        "year_th": 2517,
        "year_ce": 1974,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2517",
        "name_short": "รธน. 2517",
        "date_announced": "1974-10-07",
        "source_url": "https://hdl.handle.net/20.500.14156/290430",
        "source_type": "image_pdf",
        "filename": "15_รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2517.pdf",
        "era": "democratic_spring",
        "regime_type": "civilian",
        "notes": "หลังเหตุการณ์ 14 ตุลาคม 2516",
    },
    {
        "id": "const_2518",
        "year_th": 2518,
        "year_ce": 1975,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม พ.ศ. 2518",
        "name_short": "รธน. 2518",
        "date_announced": "1975-01-23",
        "source_url": "https://hdl.handle.net/20.500.14156/290431",
        "source_type": "image_pdf",
        "filename": "16_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม พุทธศักราช 2518.pdf",
        "era": "democratic_spring",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2519",
        "year_th": 2519,
        "year_ce": 1976,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2519",
        "name_short": "รธน. 2519",
        "date_announced": "1976-10-22",
        "source_url": "https://hdl.handle.net/20.500.14156/290432",
        "source_type": "image_pdf",
        "filename": "17_รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2519.pdf",
        "era": "democratic_spring",
        "regime_type": "military",
        "notes": "หลังเหตุการณ์ 6 ตุลาคม 2519",
    },
    {
        "id": "const_2520",
        "year_th": 2520,
        "year_ce": 1977,
        "name_th": "รัฐธรรมนูญการปกครองราชอาณาจักร พ.ศ. 2520",
        "name_short": "รธน. 2520",
        "date_announced": "1977-11-09",
        "source_url": "https://hdl.handle.net/20.500.14156/290433",
        "source_type": "image_pdf",
        "filename": "18_รัฐธรรมนูญการปกครองราชอาณาจักร พ.ศ. 2520.pdf",
        "era": "semi_democracy",
        "regime_type": "military",
        "notes": None,
    },
    {
        "id": "const_2521",
        "year_th": 2521,
        "year_ce": 1978,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พุทธศักราช 2521",
        "name_short": "รธน. 2521",
        "date_announced": "1978-12-22",
        "source_url": "https://hdl.handle.net/20.500.14156/290434",
        "source_type": "image_pdf",
        "filename": "19_รัฐธรรมนูญแห่งราชอาณาจักรไทย พุทธศักราช 2521.pdf",
        "era": "semi_democracy",
        "regime_type": "semi_military",
        "notes": None,
    },
    {
        "id": "const_2528",
        "year_th": 2528,
        "year_ce": 1985,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม พ.ศ. 2528",
        "name_short": "รธน. 2528",
        "date_announced": "1985-08-14",
        "source_url": "https://hdl.handle.net/20.500.14156/290435",
        "source_type": "image_pdf",
        "filename": "20_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม พ.ศ. 2528.pdf",
        "era": "semi_democracy",
        "regime_type": "semi_military",
        "notes": None,
    },
    {
        "id": "const_2532",
        "year_th": 2532,
        "year_ce": 1989,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 2) พ.ศ. 2532",
        "name_short": "รธน. 2532",
        "date_announced": "1989-08-30",
        "source_url": "https://hdl.handle.net/20.500.14156/290436",
        "source_type": "image_pdf",
        "filename": "21_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 2) พ.ศ. 2532.pdf",
        "era": "semi_democracy",
        "regime_type": "semi_military",
        "notes": None,
    },
    {
        "id": "const_2534a",
        "year_th": 2534,
        "year_ce": 1991,
        "name_th": "ธรรมนูญการปกครองราชอาณาจักร พุทธศักราช 2534",
        "name_short": "ธรรมนูญ 2534",
        "date_announced": "1991-03-01",
        "source_url": "https://hdl.handle.net/20.500.14156/290437",
        "source_type": "image_pdf",
        "filename": "22_ธรรมนูญการปกครองราชอาณาจักร พุทธศักราช 2534.pdf",
        "era": "modern_democracy",
        "regime_type": "military",
        "notes": "หลังรัฐประหาร 2534",
    },
    {
        "id": "const_2534b",
        "year_th": 2534,
        "year_ce": 1991,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2534",
        "name_short": "รธน. 2534",
        "date_announced": "1991-12-09",
        "source_url": "https://hdl.handle.net/20.500.14156/290439",
        "source_type": "image_pdf",
        "filename": "23_รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2534.pdf",
        "era": "modern_democracy",
        "regime_type": "military",
        "notes": None,
    },
    {
        "id": "const_2535a",
        "year_th": 2535,
        "year_ce": 1992,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 1) พุทธศักราช 2535",
        "name_short": "รธน. 2535 (ฉบับที่ 1)",
        "date_announced": "1992-06-30",
        "source_url": "https://hdl.handle.net/20.500.14156/290448",
        "source_type": "image_pdf",
        "filename": "24_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 1) พุทธศักราช 2535.pdf",
        "era": "modern_democracy",
        "regime_type": "civilian",
        "notes": "หลังพฤษภาทมิฬ 2535",
    },
    {
        "id": "const_2535b",
        "year_th": 2535,
        "year_ce": 1992,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 2) พุทธศักราช 2535",
        "name_short": "รธน. 2535 (ฉบับที่ 2)",
        "date_announced": "1992-06-30",
        "source_url": "https://hdl.handle.net/20.500.14156/290449",
        "source_type": "image_pdf",
        "filename": "25_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 2) พุทธศักราช 2535.pdf",
        "era": "modern_democracy",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2535c",
        "year_th": 2535,
        "year_ce": 1992,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 3) พุทธศักราช 2535",
        "name_short": "รธน. 2535 (ฉบับที่ 3)",
        "date_announced": "1992-06-30",
        "source_url": "https://hdl.handle.net/20.500.14156/290450",
        "source_type": "image_pdf",
        "filename": "26_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 3) พุทธศักราช 2535.pdf",
        "era": "modern_democracy",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2535d",
        "year_th": 2535,
        "year_ce": 1992,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 4) พุทธศักราช 2535",
        "name_short": "รธน. 2535 (ฉบับที่ 4)",
        "date_announced": "1992-09-12",
        "source_url": "https://hdl.handle.net/20.500.14156/290451",
        "source_type": "image_pdf",
        "filename": "27_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 4) พุทธศักราช 2535.pdf",
        "era": "modern_democracy",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2538",
        "year_th": 2538,
        "year_ce": 1995,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 5) พุทธศักราช 2538",
        "name_short": "รธน. 2538",
        "date_announced": "1995-02-10",
        "source_url": "https://hdl.handle.net/20.500.14156/290416",
        "source_type": "image_pdf",
        "filename": "28_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 5) พุทธศักราช 2538.pdf",
        "era": "modern_democracy",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2539",
        "year_th": 2539,
        "year_ce": 1996,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 6) พุทธศักราช 2539",
        "name_short": "รธน. 2539",
        "date_announced": "1996-10-22",
        "source_url": "https://hdl.handle.net/20.500.14156/290427",
        "source_type": "image_pdf",
        "filename": "29_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 6) พุทธศักราช 2539.pdf",
        "era": "modern_democracy",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2540",
        "year_th": 2540,
        "year_ce": 1997,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พุทธศักราช 2540",
        "name_short": "รธน. 2540",
        "date_announced": "1997-10-11",
        "source_url": "https://hdl.handle.net/20.500.14156/290438",
        "source_type": "image_pdf",
        "filename": "30_รัฐธรรมนูญแห่งราชอาณาจักรไทย พุทธศักราช 2540.pdf",
        "era": "modern_democracy",
        "regime_type": "civilian",
        "notes": "รัฐธรรมนูญฉบับประชาชน",
    },
    {
        "id": "const_2548",
        "year_th": 2548,
        "year_ce": 2005,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 1) พุทธศักราช 2548",
        "name_short": "รธน. 2548",
        "date_announced": "2005-07-11",
        "source_url": "https://hdl.handle.net/20.500.14156/290443",
        "source_type": "image_pdf",
        "filename": "31_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 1) พุทธศักราช 2548.pdf",
        "era": "modern_democracy",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2549",
        "year_th": 2549,
        "year_ce": 2006,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉบับชั่วคราว) พุทธศักราช 2549",
        "name_short": "รธน. 2549 (ชั่วคราว)",
        "date_announced": "2006-10-01",
        "source_url": "https://hdl.handle.net/20.500.14156/290444",
        "source_type": "image_pdf",
        "filename": "32_รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉบับชั่วคราว) พุทธศักราช 2549.pdf",
        "era": "post_coup_2006",
        "regime_type": "military",
        "notes": "หลังรัฐประหาร 19 กันยายน 2549",
    },
    # ══════════════════════════════════════════════════════
    # TEXT PDFs — ดึงข้อความด้วย PyMuPDF / pdfplumber (ไฟล์ที่ 33–38)
    # ══════════════════════════════════════════════════════
    {
        "id": "const_2550",
        "year_th": 2550,
        "year_ce": 2007,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พุทธศักราช 2550",
        "name_short": "รธน. 2550",
        "date_announced": "2007-08-24",
        "source_url": "https://hdl.handle.net/20.500.14156/290445",
        "source_type": "text_pdf",
        "filename": "33_รัฐธรรมนูญแห่งราชอาณาจักรไทย พ.ศ. 2550.pdf",
        "era": "post_coup_2006",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2554a",
        "year_th": 2554,
        "year_ce": 2011,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 1) พุทธศักราช 2554",
        "name_short": "รธน. 2554 (ฉบับที่ 1)",
        "date_announced": "2011-03-04",
        "source_url": "https://hdl.handle.net/20.500.14156/290446",
        "source_type": "text_pdf",
        "filename": "34_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 1) พุทธศักราช 2554.pdf",
        "era": "post_coup_2006",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2554b",
        "year_th": 2554,
        "year_ce": 2011,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 2) พุทธศักราช 2554",
        "name_short": "รธน. 2554 (ฉบับที่ 2)",
        "date_announced": "2011-03-04",
        "source_url": "https://hdl.handle.net/20.500.14156/290447",
        "source_type": "text_pdf",
        "filename": "35_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 2) พุทธศักราช 2554.pdf",
        "era": "post_coup_2006",
        "regime_type": "civilian",
        "notes": None,
    },
    {
        "id": "const_2557",
        "year_th": 2557,
        "year_ce": 2014,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉบับชั่วคราว) พุทธศักราช 2557",
        "name_short": "รธน. 2557 (ชั่วคราว)",
        "date_announced": "2014-07-22",
        "source_url": "https://hdl.handle.net/20.500.14156/380874",
        "source_type": "text_pdf",
        "filename": "36_รัฐธรรมนูญแห่งราชอาณาจักรไทย (ฉบับชั่วคราว) พุทธศักราช 2557.pdf",
        "era": "post_coup_2014",
        "regime_type": "military",
        "notes": "หลังรัฐประหาร 22 พฤษภาคม 2557",
    },
    {
        "id": "const_2560",
        "year_th": 2560,
        "year_ce": 2017,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย พุทธศักราช 2560",
        "name_short": "รธน. 2560",
        "date_announced": "2017-04-06",
        "source_url": "https://hdl.handle.net/20.500.14156/507273",
        "source_type": "text_pdf",
        "filename": "37_รัฐธรรมนูญแห่งราชอาณาจักรไทย พุทธศักราช 2560.pdf",
        "era": "post_coup_2014",
        "regime_type": "semi_military",
        "notes": "รัฐธรรมนูญที่ใช้ในปัจจุบัน",
    },
    {
        "id": "const_2564",
        "year_th": 2564,
        "year_ce": 2021,
        "name_th": "รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 1) พุทธศักราช 2564",
        "name_short": "รธน. 2564",
        "date_announced": "2021-11-21",
        "source_url": "https://hdl.handle.net/20.500.14156/588896",
        "source_type": "text_pdf",
        "filename": "38_รัฐธรรมนูญแห่งราชอาณาจักรไทย แก้ไขเพิ่มเติม (ฉบับที่ 1) พุทธศักราช 2564.pdf",
        "era": "post_coup_2014",
        "regime_type": "semi_military",
        "notes": None,
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────────────────────────────────────


def get_constitution_by_id(constitution_id: str) -> dict | None:
    """ดึง metadata ของรัฐธรรมนูญจาก ID"""
    for c in CONSTITUTIONS:
        if c["id"] == constitution_id:
            return c
    return None


def get_image_pdfs() -> list[dict]:
    """ดึงรายการรัฐธรรมนูญที่เป็น Image PDF (ต้องทำ OCR)"""
    return [c for c in CONSTITUTIONS if c["source_type"] == "image_pdf"]


def get_text_pdfs() -> list[dict]:
    """ดึงรายการรัฐธรรมนูญที่เป็น Text PDF (ดึงข้อความได้โดยตรง)"""
    return [c for c in CONSTITUTIONS if c["source_type"] == "text_pdf"]


def get_constitutions_by_era(era: str) -> list[dict]:
    """ดึงรายการรัฐธรรมนูญตามยุคสมัย"""
    return [c for c in CONSTITUTIONS if c["era"] == era]


if __name__ == "__main__":
    image_pdfs = get_image_pdfs()
    text_pdfs = get_text_pdfs()
    print(f"รัฐธรรมนูญทั้งหมด    : {len(CONSTITUTIONS)} ฉบับ")
    print(f"Image PDFs (OCR)    : {len(image_pdfs)} ฉบับ (ไฟล์ 1–32, พ.ศ. 2475–2549)")
    print(f"Text PDFs (Extract) : {len(text_pdfs)} ฉบับ (ไฟล์ 33–38, พ.ศ. 2550–2564)")
    print()
    print("Image PDFs:")
    for c in image_pdfs:
        print(f"  [{c['year_th']}] {c['name_short']}")
    print()
    print("Text PDFs (first 5):")
    for c in text_pdfs[:5]:
        print(f"  [{c['year_th']}] {c['name_short']}")
