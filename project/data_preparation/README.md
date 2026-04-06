# Data Preparation Pipeline
## โครงการวิเคราะห์รัฐธรรมนูญไทย 20 ฉบับ (CPE232)

---

## ภาพรวม (Overview)

งานในส่วน **Data Preparation** มีหน้าที่แปลงเอกสารรัฐธรรมนูญไทยทั้งหมดให้อยู่ในรูปแบบข้อความดิจิทัลที่พร้อมสำหรับการวิเคราะห์ต่อไป เนื่องจากรัฐธรรมนูญไทยมีรูปแบบที่ต่างกันตามยุคสมัย จึงแบ่งการประมวลผลออกเป็น **2 เส้นทาง (Pipeline)**

| ประเภท | ช่วงปี พ.ศ. | วิธีการ | จำนวน |
|--------|-----------|---------|-------|
| **PDF รูปภาพ (Image PDF)** | 2475 – 2502 | OCR ด้วย **Typhoon OCR 1.5** | 12 ฉบับ |
| **PDF ข้อความ (Text PDF)** | 2511 – 2564 | Text Extraction ด้วย **PyMuPDF / pdfplumber** | 26 ฉบับ |

---

## ภาพรวม Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│                       INPUT: PDF Files (38 files)                   │
└─────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│              STEP 0: PDF Classification (จำแนกประเภท PDF)          │
│          ตรวจสอบว่าแต่ละ PDF เป็นแบบรูปภาพหรือแบบข้อความ           │
└─────────────────────────────────────────────────────────────────────┘
          │                                          │
          ▼                                          ▼
┌──────────────────────┐                  ┌──────────────────────────┐
│   IMAGE PDF PATH     │                  │    TEXT PDF PATH         │
│   (2475–2502)        │                  │    (2511–2564)           │
│                      │                  │                          │
│ STEP 1: ตรวจนับหน้า  │                  │ STEP 1: ตรวจ Encoding   │
│   (pdfinfo)          │                  │   ของไฟล์ PDF            │
│         │            │                  │         │                │
│         ▼            │                  │         ▼                │
│ STEP 2: OCR ทีละหน้า │                  │ STEP 2: Extract Text    │
│  (Typhoon OCR 1.5)   │                  │   (PyMuPDF/pdfplumber)  │
│   ▸ Rate limit aware │                  │         │                │
│   ▸ Retry on error   │                  │         ▼                │
│   ▸ Cache ผลลัพธ์    │                  │ STEP 3: Fix Encoding    │
│         │            │                  │   & Thai Unicode        │
│         ▼            │                  │         │                │
│ STEP 3: รวม Markdown │                  └─────────┼────────────────┘
│   ทุกหน้าเข้าด้วยกัน│                            │
└──────────┬───────────┘                            │
           │                                        │
           └────────────────┬───────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│         STEP 4: Post-Processing & Text Cleaning                     │
│   ▸ ลบ Header/Footer ราชกิจจานุเบกษา                               │
│   ▸ แยกโครงสร้าง หมวด / มาตรา / วรรค                              │
│   ▸ Normalize Unicode ภาษาไทย (NFC)                                │
│   ▸ แปลงเลขไทย → เลขอารบิก                                         │
└─────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│         STEP 5: Validation & Quality Check                          │
│   ▸ ตรวจสอบว่าข้อความไม่ว่างเปล่า                                  │
│   ▸ ตรวจสอบ character ที่ผิดปกติจาก OCR error                      │
│   ▸ สร้าง QA Report สรุปคุณภาพ                                     │
└─────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│         STEP 6: Structured Output                                   │
│   ▸ JSON (ต่อฉบับ + รวมทั้งหมด)                                    │
│   ▸ CSV (สำหรับ EDA)                                               │
│   ▸ Plain Text (สำหรับ NLP)                                        │
└─────────────────────────────────────────────────────────────────────┘
```

---

## โครงสร้าง Directory

```
project/
└── data_preparation/
    ├── README.md                  ← ไฟล์นี้ (เอกสาร Pipeline)
    ├── requirements.txt           ← Python dependencies
    ├── .env.example               ← ตัวอย่างการตั้งค่า API Key
    ├── config.py                  ← Metadata ของรัฐธรรมนูญทั้งหมด
    ├── 01_ocr_pipeline.py         ← OCR สำหรับ Image PDF (2475–2502)
    ├── 02_text_extraction.py      ← Text Extraction สำหรับ Text PDF (2511–2564)
    ├── 03_validate_output.py      ← ตรวจสอบคุณภาพผลลัพธ์
    ├── run_pipeline.py            ← Script หลักสำหรับรัน Pipeline ทั้งหมด
    └── data/
        ├── raw_pdfs/              ← วางไฟล์ PDF ต้นฉบับที่นี่
        ├── ocr_output/            ← ผลลัพธ์ OCR (Markdown ต่อหน้า)
        ├── extracted_text/        ← ผลลัพธ์ Text Extraction
        └── processed/             ← ผลลัพธ์สุดท้าย (JSON, CSV, TXT)
```

---

## รัฐธรรมนูญที่ต้องทำ OCR (Image PDFs)

| ลำดับ | ชื่อ | ปี พ.ศ. | File ID |
|-------|------|--------|---------|
| 1 | รัฐธรรมนูญแห่งราชอาณาจักรสยาม | 2475 | `const_2475` |
| 2 | รัฐธรรมนูญแก้ไขเพิ่มเติมว่าด้วยนามประเทศ | 2482 | `const_2482` |
| 3 | รัฐธรรมนูญแก้ไขเพิ่มเติมว่าด้วยบทเฉพาะกาล | 2483 | `const_2483` |
| 4 | รัฐธรรมนูญแก้ไขเพิ่มเติมว่าด้วยการเลือกตั้ง | 2485 | `const_2485` |
| 5 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2489 | `const_2489` |
| 6 | รัฐธรรมนูญ (ฉะบับชั่วคราว) | 2490a | `const_2490a` |
| 7 | รัฐธรรมนูญ (ฉบับชั่วคราว) แก้ไขเพิ่มเติม | 2490b | `const_2490b` |
| 8 | รัฐธรรมนูญ (ฉะบับชั่วคราว) แก้ไขเพิ่มเติม ฉบับที่ 2 | 2491a | `const_2491a` |
| 9 | รัฐธรรมนูญ (ฉบับชั่วคราว) แก้ไขเพิ่มเติม ฉบับที่ 3 | 2491b | `const_2491b` |
| 10 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2492 | `const_2492` |
| 11 | รัฐธรรมนูญ พุทธศักราช 2475 แก้ไขเพิ่มเติม พุทธศักราช 2495 | 2495 | `const_2495` |
| 12 | ธรรมนูญการปกครองราชอาณาจักร | 2502 | `const_2502` |

---

## รัฐธรรมนูญที่ใช้ Text Extraction (Text PDFs)

| ลำดับ | ชื่อ | ปี พ.ศ. | File ID |
|-------|------|--------|---------|
| 1 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2511 | `const_2511` |
| 2 | ธรรมนูญการปกครองราชอาณาจักร | 2515 | `const_2515` |
| 3 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2517 | `const_2517` |
| 4 | รัฐธรรมนูญแก้ไขเพิ่มเติม | 2518 | `const_2518` |
| 5 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2519 | `const_2519` |
| 6 | รัฐธรรมนูญการปกครองราชอาณาจักร | 2520 | `const_2520` |
| 7 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2521 | `const_2521` |
| 8 | รัฐธรรมนูญแก้ไขเพิ่มเติม | 2528 | `const_2528` |
| 9 | รัฐธรรมนูญแก้ไขเพิ่มเติม (ฉบับที่ 2) | 2532 | `const_2532` |
| 10 | ธรรมนูญการปกครองราชอาณาจักร | 2534a | `const_2534a` |
| 11 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2534b | `const_2534b` |
| 12–15 | รัฐธรรมนูญแก้ไขเพิ่มเติม ฉบับที่ 1–4 | 2535 | `const_2535a`–`d` |
| 16 | รัฐธรรมนูญแก้ไขเพิ่มเติม (ฉบับที่ 5) | 2538 | `const_2538` |
| 17 | รัฐธรรมนูญแก้ไขเพิ่มเติม (ฉบับที่ 6) | 2539 | `const_2539` |
| 18 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2540 | `const_2540` |
| 19 | รัฐธรรมนูญแก้ไขเพิ่มเติม (ฉบับที่ 1) | 2548 | `const_2548` |
| 20 | รัฐธรรมนูญ (ฉบับชั่วคราว) | 2549 | `const_2549` |
| 21 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2550 | `const_2550` |
| 22–23 | รัฐธรรมนูญแก้ไขเพิ่มเติม ฉบับที่ 1–2 | 2554 | `const_2554a`–`b` |
| 24 | รัฐธรรมนูญ (ฉบับชั่วคราว) | 2557 | `const_2557` |
| 25 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2560 | `const_2560` |
| 26 | รัฐธรรมนูญแก้ไขเพิ่มเติม (ฉบับที่ 1) | 2564 | `const_2564` |

---

## การติดตั้ง (Environment Setup)

### 1. สร้าง Virtual Environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

### 2. ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

### 3. ตั้งค่า API Key

1. สมัครบัญชีที่ [https://opentyphoon.ai](https://opentyphoon.ai) เพื่อรับ API Key
2. คัดลอกไฟล์ `.env.example` เป็น `.env`
3. ใส่ API Key ลงใน `.env`

```bash
cp .env.example .env
# แก้ไข .env ด้วย editor ของคุณ
```

### 4. ติดตั้ง Poppler (Windows)

Poppler จำเป็นสำหรับการแปลง PDF เป็นรูปภาพ

- ดาวน์โหลดจาก: https://github.com/oschwartz10612/poppler-windows/releases
- แตกไฟล์และเพิ่ม path ของ `bin/` ลงใน System PATH

---

## วิธีรัน Pipeline

### รันทั้งหมดในครั้งเดียว

```bash
python run_pipeline.py
```

### รันแต่ละขั้นตอนแยกกัน

```bash
# ขั้นตอนที่ 1: OCR สำหรับ Image PDFs (2475-2502)
python 01_ocr_pipeline.py

# ขั้นตอนที่ 2: Text Extraction สำหรับ Text PDFs (2511-2564)
python 02_text_extraction.py

# ขั้นตอนที่ 3: ตรวจสอบคุณภาพ
python 03_validate_output.py
```

### Options

```bash
# รัน OCR เฉพาะบางฉบับ
python 01_ocr_pipeline.py --ids const_2475 const_2492

# ข้ามไฟล์ที่ประมวลผลไปแล้ว (resume)
python 01_ocr_pipeline.py --skip-existing

# เปิด verbose mode
python run_pipeline.py --verbose
```

---

## Output Format

### JSON (ต่อฉบับ)

ไฟล์ชื่อ `const_XXXX.json` บันทึกใน `data/processed/`

```json
{
  "id": "const_2475",
  "year_th": 2475,
  "year_ce": 1932,
  "name": "รัฐธรรมนูญแห่งราชอาณาจักรสยาม พ.ศ. 2475",
  "date_announced": "1932-12-10",
  "source_url": "https://hdl.handle.net/20.500.14156/290453",
  "source_type": "image_pdf",
  "processing_method": "typhoon-ocr-1.5",
  "total_pages": 14,
  "era": "early_democracy",
  "regime_type": "civilian",
  "pages": [
    {
      "page_num": 1,
      "raw_markdown": "# รัฐธรรมนูญ...\n\n...",
      "has_figure": false
    }
  ],
  "full_text": "รัฐธรรมนูญแห่งราชอาณาจักรสยาม...",
  "articles": [
    {
      "article_num": 1,
      "chapter": null,
      "text": "อำนาจอธิปไตยสูงสุดของประเทศนั้นเป็นของราษฎรทั้งหลาย"
    }
  ],
  "metadata": {
    "total_articles": 68,
    "total_chapters": 0,
    "word_count": 3500,
    "ocr_quality_score": 0.95
  }
}
```

### CSV (รวมทุกฉบับ)

ไฟล์ `all_constitutions.csv` สำหรับนำเข้า EDA โดยตรง

| id | year_th | year_ce | name | source_type | total_pages | total_articles | word_count | era |
|----|---------|---------|------|-------------|-------------|----------------|------------|-----|
| const_2475 | 2475 | 1932 | ... | image_pdf | 14 | 68 | 3500 | early_democracy |

---

## ข้อควรระวัง (Important Notes)

### Rate Limit ของ Typhoon OCR API

- **2 requests/second** และ **20 requests/minute**
- Pipeline มีการจัดการ rate limit อัตโนมัติ (time.sleep + exponential backoff)
- ประมาณเวลาประมวลผล: ~3–5 ชั่วโมงสำหรับรัฐธรรมนูญ 12 ฉบับ (ขึ้นอยู่กับจำนวนหน้า)

### การ Cache ผลลัพธ์

- ผลลัพธ์ OCR แต่ละหน้าจะถูก cache ใน `data/ocr_output/<id>/page_<n>.md`
- หากรัน Pipeline ซ้ำ จะข้ามหน้าที่ cache ไว้แล้ว (ไม่เสีย API request)
- ใช้ `--force-reprocess` เพื่อบังคับประมวลผลใหม่

### ปัญหาที่พบบ่อยจาก OCR

| ปัญหา | ตัวอย่าง | วิธีแก้ |
|-------|---------|---------|
| ตัวอักษรคล้ายกัน | ก/ท, ว/ส | Post-processing dictionary |
| เลขไทย/อารบิก | ๑๒๓ → 123 | `pythainlp.util.digit_to_eng()` |
| วรรณยุกต์หาย | มาตรา → มาตรา | Unicode normalization NFC |
| บรรทัดแตก | คำยาว\nต่อ | Line merger |

---

## แหล่งข้อมูลเพิ่มเติม

- **Typhoon OCR Documentation**: https://docs.opentyphoon.ai/en/ocr/
- **Typhoon OCR 1.5 Model**: https://huggingface.co/typhoon-ai/typhoon-ocr1.5-2b
- **แหล่งข้อมูลรัฐธรรมนูญ**: https://catalog.parliament.go.th/dataset/12_01
- **PyMuPDF Documentation**: https://pymupdf.readthedocs.io/
- **pdfplumber Documentation**: https://github.com/jsvine/pdfplumber

---

*CPE232 Data Models — Final Project — กลุ่ม Constitution*