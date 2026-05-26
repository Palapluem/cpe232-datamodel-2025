

**รายงานผลดำเนินการโครงงาน (Final Project)**

**การวิเคราะห์รัฐธรรมนูญ 20 ฉบับของประเทศไทย**

**Twenty Constitutions Analysis : Analyze of 20 Thai Constitutions.**

**คณะผู้จัดทำ**

| 67070501003 | กันต์ธีร์ | ดวงมณี |
| :---- | :---- | :---- |
| **67070501027** | **นัธทวัฒน์** | **ปริมสิริคุณาวุฒิ** |
| **67070501042** | **วิศิษฐ์** | **สุวรรณเนาว์** |
| **67070501045** | **ศุภวิชญ์** | **มารยาท** |
| **67070501067** | **พลวริษฐ์** | **วัฒนเหมรัตน์** |

**เสนอ**

**ดร. สัญญสิริ ธารประดับ**

**ภาคเรียนที่ 2 ปีการศึกษา 2568**

**รายวิชา CPE232 แบบจำลองข้อมูล (Data Models)**

**ภาควิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์**

**มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี**

# **สารบัญ** {#สารบัญ}

---

| [สารบัญ](#bookmark=kix.y29tdxmhz6nx) | ก |
| :---- | ----: |
| [สารบัญรูปภาพ](#bookmark=kix.5lkatkwyif8s) | ค |
| [สารบัญตาราง](#bookmark=kix.mdqj754kp2kk) | ง |
| [1\. บทนำ (Introduction)](#bookmark=kix.qh38jl93eteo) | 1-2 |
| [1.1 ระบบไฟจราจร(Traffic light system)](#bookmark=kix.z1geje3qjhxi) | 1 |
| [1.2 Field Programmable Gate Array (FPGA)](#bookmark=kix.6bn9e24s77ly) | 1 |
| [1.3 Digilent Basys 3™ Artix-7 FPGA Trainer Board](#bookmark=kix.usrs447n399h) | 2 |
| [2\. วัตถุประสงค์ (Objective)](#bookmark=kix.imf4gxv1cuu4) | 2 |
| [3\. อุปกรณ์ที่ใช้ (Equipment)](#bookmark=kix.3rfj1wd7ect2) | 3 |
| 3[.1. ซอฟต์แวร์ (Software)](#bookmark=kix.edy79zajm1wg) | 3 |
| 3[.2. ฮาร์ดแวร์ (Hardware)](#bookmark=kix.udwu3db24fvm) | 3 |
| [4\. ส่วนประกอบวงจร](#bookmark=kix.3xutk3yhea1m) | 4-6 |
| [4.1 Input Switch (Controller)](#bookmark=kix.7x6xje5h3icj) | 5 |
| [4.2 Field Programmable Gate Array (FPGA)](#bookmark=kix.vo41pepiio3m) | 5 |
| [4.3 Monitor display (รองรับสาย VGA)](#bookmark=kix.ekly11vhgw7m) | 6 |
| [5\. หลักการทำงาน](#bookmark=kix.60na0gg6y957)  | 7-13 |
| [5.1 ภาพรวมการออกแบบวงจรตรรกะ (Logic Design Overview)](#bookmark=kix.hd68gml2lgn2) | 7 |
| [5.2 โครงสร้างสถาปัตยกรรมภายใน (System Architecture)](#bookmark=kix.saa1dpwboxmh) | 8 |
| [5.3 ระบบควบคุมสัญญาณไฟจราจร (Traffic Light Control System)](#bookmark=kix.syo41ft3s70y) | 9 |
| [5.3.1 การจัดการอินพุตและเวลา (Input Decoding & Timing Calculator)](#bookmark=kix.ejhscahxnm9d) | 10 |
| [5.3.2 เครื่องจักรสถานะโหมดอัตโนมัติ (Automatic Mode FSM)](#bookmark=kix.eskdnk7947ta) | 10 |
| [5.3.3 เครื่องจักรสถานะโหมดควบคุมด้วยมือ (Manual Mode FSM)](#bookmark=kix.5ghq46sxopxx) | 12 |
| [5.3.4 ระบบความปลอดภัยและการเปลี่ยนโหมด (Safety & Mode Transition)](#bookmark=kix.xowh6yl1huxd) | 12 |
| [5.3.5 ตรรกะเอาต์พุต (Output Logic)](#bookmark=kix.ooi341e9oyc1) | 13 |
| [5.4 ระบบแสดงผลกราฟิก (Graphic Display System)](#bookmark=kix.uc0kmvtqk01k) | 13 |
| [5.4.1 การกำเนิดสัญญาณภาพ (Signal Generation)](#bookmark=kix.wtxxwjaqfpcs) | 13 |
| [5.4.2 การสร้างภาพกราฟิกและข้อความ (Rendering Pipeline)](#bookmark=kix.vz16g6d6cgfk) | 13 |
| 6\. ผลลัพธ์การทำงาน | 14-17 |
| [7\. ปัญหา อุปสรรคที่พบ และแนวทางแก้ไข](#bookmark=kix.eej5szjh516o) | 18 |
| [8\. สรุป](#bookmark=kix.sjkon7kpfqxi) | 18 |
| [9\. อ้างอิง](#bookmark=kix.t3kx1j2pg7l1) | 18 |
| [10\. ภาคผนวก](#bookmark=kix.nnrndiz7r5ep) | 19 |

# **สารบัญรูปภาพ**

---

| [รูปที่ 1 Digilent Basys3 FPGA Development Board](#bookmark=kix.ymoidy9tsh2y)     | 3 |
| :---- | ----: |
| [**รูปที่ 2** สาย VGA](#bookmark=kix.el647kaq7a4a)  | 4 |
| [**รูปที่ 3** VGA Monitor](#bookmark=kix.ug49v0mf81d7)  | 4 |
| [**รูปที่ 4** แผนภาพแสดงองค์ประกอบของวงจร](#bookmark=kix.vj05iavnhhht)  | 4 |
| [**รูปที่ 5** ภาพสวิตซ์ที่มีการใช้งานเพื่อรับข้อมูล](#bookmark=kix.8j6f4zyq0gft) | 5 |
| [**รูปที่ 6** แผนภาพแสดงหลักการแสดงภาพของ VGA Monitor](#bookmark=kix.7dt25l9mx5ax)   | 6 |
| [**รูปที่ 7** แผนภาพบล็อกอินพุตและเอาต์พุตของวงจรตรรกะหลัก (Main Logic Interface)](#bookmark=kix.d40485eqam8)      | 8 |
| [**รูปที่ 8**  แผนภาพแสดงการเชื่อมต่อระหว่างโมดูลภายใน FPGA (Block Diagram)](#bookmark=kix.bul0mtqrkhlh)    | 9 |
| [**รูปที่ 9**  ผังการทำงานภายในของระบบควบคุมไฟจราจร (Traffic Light Controller Logic Flow)](#bookmark=kix.pavahto2it6b) | 9 |
| [**รูปที่ 10** แผนภาพสถานะโหมดอัตโนมัติ (Automatic Mode State Diagram)](#bookmark=kix.m563le780307) | 11 |
| [**รูปที่ 11** แผนภาพสถานะโหมดควบคุมด้วยมือ (Manual Mode State Diagram)](#bookmark=kix.x6vlo0n4ttxb) | 12 |
| [**รูปที่ 12** รูปแสดงผลสถานะเริ่มต้นบนจอ VGA](#bookmark=kix.yvs2thbjxy0b) | 14 |
| [**รูปที่ 13** รูปบอร์ดแสดงอินพุตสำหรับเปลี่ยนโหมด](#bookmark=kix.fwcmjs4tyoao)   | 14 |
| [**รูปที่ 14** รูปแสดงผลสถานะเมื่อใช้งานโหมด Auto1](#bookmark=kix.4gdw9htb75l7) | 15 |
| [**รูปที่ 15** รูปแสดงผลสถานะเมื่อใช้งานโหมด Auto2](#bookmark=kix.33pay7in93zg) | 15 |
| [**รูปที่ 16** รูปแสดงผลสถานะเมื่อใช้งานโหมด Auto3](#bookmark=kix.agc31x9otzxw) | 15 |
| [**รูปที่ 17**](#bookmark=kix.y0s2q8uw7lkl) รูปแสดงปุ่มที่ใช้ควบคุมในโหมด  Manual | 16 |
| [**รูปที่ 18** รูปแสดงผลสถานะเมื่อสลับโหมด Auto-Manual](#bookmark=kix.mqexhvx3evk9) | 16 |
| [**รูปที่ 19** รูปแสดงผลสถานะเมื่อใช้งาน Pair Mode FSM1](#bookmark=kix.ru27fzgb0o6g) | 17 |
| [**รูปที่ 20** รูปแสดงผลสถานะเมื่อใช้งาน Pair Mode FSM2](#bookmark=kix.ueblegucmjk) | 17 |
| [**รูปที่ 21** รูปแสดงผลสถานะเมื่อใช้งาน Pair Mode FSM3](#bookmark=kix.tnyk9bfedzgl) | 17 |

# **สารบัญตาราง**

---

[**ตาราง 1** รายการเครื่องมือซอฟต์แวร์ที่ใช้ในการพัฒนา](#bookmark=kix.pra6i4y65cm)						           3	

[**ตาราง 2** รายการเครื่องมือฮาร์ดแวร์ที่ใช้ในการพัฒนา](#bookmark=kix.q5patwelan5n)						       3-4

# 

# **บทที่ 1 บทนำ**

# ---

**1.1 ที่มาและความสำคัญ**

ประเทศไทยมีรัฐธรรมนูญรวมทั้งสิ้น 20 ฉบับ นับตั้งแต่ปี พ.ศ. 2475 จนถึงปัจจุบัน ซึ่งถือว่าเยอะมากที่สุดเมื่อเทียบกับประเทศที่ปกครองในระบอบประชาธิปไตย รัฐธรรมนูญแต่ละฉบับสะท้อนบริบทการเมืองที่แตกต่างกัน ไม่ว่าจะรัฐบาลพลเรือน คณะรัฐประหาร หรือสภาเฉพาะกาล ดังนั้นโครงงานนี้มีเป้าหมายในการรวบรวม ดิจิทัลไลซ์ และวิเคราะห์รัฐธรรมนูญทั้ง 20 ฉบับในฐานะคลังข้อความ (Text Corpus) โดยใช้เทคนิค OCR, NLP, และ ML เพื่อตอบคำถามหลักว่า “รัฐธรรมนูญไทยเปลี่ยนแปลงอย่างไรตลอด 9 ทศวรรษ และการเปลี่ยนนี้สะท้อนประวัติศาสตร์การเมืองไทยอย่างไร?” นอกจากนี้ยังนำข้อมูล Structured จาก [Constituteproject.org](http://Constituteproject.org) ซึ่งจัดทำดัชนีสิทธิ์ตามรัฐธรรมนูญของแต่ละประเทศ มาใช้เปรียบเทียบการคุ้มครองสิทธิในรัฐธรรมนูญไทยแต่ละฉบับเชิงปริมาณ

**1.2 วัตถุประสงค์**

	โครงงานนี้มีวัตถุประสงค์หลักในการดำเนินการวิเคราะห์รัฐธรรมนูญ 20 ฉบับของไทย โดยมีเป้าหมายที่สำคัญดังนี้:

1. เพื่อสร้างคลังข้อความ (Corpus) ของรัฐธรรมนูญ 20 ฉบับ โดยใช้ OCR และการดึงข้อมูลจากไฟล์ PDF  
2. เพื่อวิเคราะห์โครงสร้าง ได้แก่ จำนวนมาตรา ความยาว การแบ่งหมวด และความถี่ในการแก้ไขเพิ่มเติม  
3. เพื่อหาการเปลี่ยนแปลงเชิงหัวข้อและภาษา ระหว่างแต่ละยุคการเมือง  
4. เพื่อวัดและเปรียบเทียบสิทธิในรัฐธรรมนูญแต่ละฉบับ จากดัชนีของ [constituteproject.org](http://constituteproject.org)  
5. เพื่อวัดความคล้ายคลึงระหว่างรัฐธรรมนูญแต่ละฉบับ  
6. เพื่อสร้างโมเดล Machine Learning ในการวิเคราะห์โครงสร้าง โดยประยุกต์ใช้ความรู้จากวิชา CPE232 Data Models ในทุกขั้นตอน

**1.3 ขอบเขตของโครงงาน**

โครงงานนี้มุ่งเน้นรวบรวมและวิเคราะห์เฉพาะ **รัฐธรรมนูญและธรรมนูญการปกครอง** ของประเทศไทย ที่ประกาศใช้ในราชกิจจานุเบกษา ตั้งแต่ปี พ.ศ. 2475 ถึงปัจจุบัน จำนวน 20 ฉบับหลัก (รวมเอกสารแก้ไขเพิ่มเติมเป็น 38 ไฟล์) โดยการประมวลผลข้อมูลจำกัดอยู่ที่กระบวนการดึงข้อความ (Text Extraction) การแปลงภาพเป็นข้อความ (OCR) การจัดการโครงสร้างข้อมูล (JSON Structure) และการ เตรียมพร้อมไปสู่การสร้างโมเดลจำแนกหัวข้อ (Topic Modeling)

**1.4 เครื่องมือที่ใช้ในการพัฒนา**

สำหรับการพัฒนาและวิเคราะห์ข้อมูลในโครงงานการวิเคราะห์รัฐธรรมนูญ 20 ฉบับของประเทศไทย ได้เลือกใช้เครื่องมือและเทคโนโลยีหลักดังต่อไปนี้:

* Python / Jupyter Notebook: เครื่องมือหลักในการเขียนและรันท่อข้อมูล (Data Pipeline)  
* Typhoon OCR API 1.5: โมเดลปัญญาประดิษฐ์สกัดอักษรจากภาพสำหรับภาษาไทย  
* PyMuPDF (fitz) / pdfplumber: ไลบรารีสำหรับสกัดข้อความจากไฟล์ Text PDF  
* Pandas: สำหรับจัดการตารางข้อมูลและโครงสร้างข้อมูลเบื้องต้น  
* JSON: โครงสร้างข้อมูลที่ใช้จัดเก็บ Metadata และเนื้อหา  
* PyThaiNLP / Attacut: สำหรับการทำ Tokenization และทำความสะอาดภาษาไทย  
* Scikit-learn: สำหรับ Feature Extraction และ Machine Learning

**บทที่ 2 การสำรวจข้อมูลเบื้องต้น**

---

ก่อนเริ่มการประมวลผล คณะผู้จัดทำได้สำรวจชุดข้อมูลรัฐธรรมนูญที่รวบรวมมา เพื่อออกแบบโครงสร้างข้อมูล (Data Model) ให้เหมาะสมที่สุด ซึ่งรายละเอียดสำหรับการสำรวจข้อมูลเบื้องต้น มีดังนี้

**2.1 คำอธิบายข้อมูล**

ข้อมูลชั้นต้น (Primary Data) คือรัฐธรรมนูญและธรรมนูญการปกครองของไทย จัดทำโดย สำนักวิชาการ สำนักงานเลขาธิการสภาผู้แทนราษฎร ซึ่งถูกเก็บไว้ในระบบคลังสารสนเทศรัฐสภา โดยเผยแพร่ภายใต้สัญญาอนุญาต Creative Commons (CC BY-NC-ND 4.0) ข้อมูลต้นฉบับอยู่ในรูปแบบไฟล์เอกสาร (PDF) ซึ่งมีทั้งแบบภาพสแกน (สำหรับยุคเก่า) และข้อความดิจิทัล (ยุคปัจจุบัน)

**2.2 จำนวนรายการข้อมูล**

ชุดข้อมูลที่ถูกนำมาวิเคราะห์ประกอบด้วยเอกสาร 38 ไฟล์ (แบ่งเป็น 32 Image PDFs และ 6 Text PDFs) ซึ่งประกอบเป็นรัฐธรรมนูญ 20 ฉบับหลัก และฉบับแก้ไขเพิ่มเติม โดยมีปริมาณข้อความรวมโดยประมาณ 61,301 คำ

**2.3 หมวดหมู่ของข้อมูล**

เพื่อให้การนำข้อมูลไปใช้ง่ายขึ้น ข้อมูลถูกจัดกลุ่มไว้ด้วย Metadata (JSON Schema) ที่สำคัญ ดังนี้:

* **id**: รหัสอ้างอิงของเอกสาร  
* **year\_th / year\_ce**: ปีพุทธศักราชและคริสต์ศักราชที่ประกาศใช้  
* **name\_short**: ชื่อเรียกสั้น ๆ  
* **source\_type**: ประเภทของไฟล์เอกสาร (image\_pdf หรือ text\_pdf)  
* **era / regime\_type**: ยุคการเมืองและระบอบการปกครองในขณะนั้น  
* **full\_text**: ข้อความทั้งหมดที่สกัดมาได้  
* **metadata**: รายละเอียดปลีกย่อย เช่น จำนวนอักขระ, จำนวนหน้า, และจำนวนคำโดยประมาณ

**2.4 คุณภาพของข้อมูล**

จากการสำรวจคุณภาพเชิงลึก พบปัญหาทางข้อมูลที่สำคัญ 2 ประการ ได้แก่:

1. # **Outdated Font Encoding (สระอำแยกร่าง)**: ในเอกสารยุคหลัง (พ.ศ. 2550 \- 2564\) มีการเข้ารหัสตัวสระอำด้วยช่องว่าง (Zero-width space) ประกอบสระอา ทิ้งให้คำผิดเพี้ยน เช่น "จ านวน" (แทนที่จะเป็น จำนวน)

2. # **Noise and Redundancy**: แต่ละหน้าของเอกสารมักมีข้อความส่วนหัวและส่วนท้าย (เช่น "ราชกิจจานุเบกษา" เลขหน้า เล่ม ตอนที่) ซึ่งไม่เกี่ยวกับตัวบทกฎหมายและจะไปรบกวนโมเดล Machine Learning

# **บทที่ 3 การเตรียมและการจัดการข้อมูล**

---

ส่วนนี้คือกระบวนการหลักที่ดำเนินการเสร็จสิ้นแล้ว โดยแบ่งเป็นการดึงข้อมูลดิบออกจากไฟล์ (Data Extraction) และการทำความสะอาดพร้อมจัดโครงสร้าง (Data Structuring)

## **3.1 การสกัดข้อความจากเอกสาร PDF (Data Extraction)**

เนื่องจากรูปแบบไฟล์มีความแตกต่างกัน กระบวนการสกัดจึงถูกแบ่งเป็น 2 วิธี:

1. **สำหรับข้อมูลกลุ่ม พ.ศ. 2475–2548 (Image PDF)**: เนื่องจากเอกสารกลุ่มนี้เป็นไฟล์ภาพสแกนจากเอกสารรัฐธรรมนูญเก่าที่เป็นแบบพิมพ์ดีดแล้วเก็บในรูปแบบรูปภาพ จึงต้องทำการสกัดตัวอักษรด้วยเทคโนโลยี Optical Character Recognition (OCR) โดยทางผู้จัดทำเลือกใช้ Typhoon OCR API (v1.5x-70b-vision-instruct) เนื่องจากเป็นโมเดลปัญญาประดิษฐ์ที่ถูกฝึกมาเพื่อรองรับโครงสร้างภาษาไทยได้ดีเยี่ยม

**ตาราง 1** โค้ดสำหรับการสกัดตัวอักษรด้วยเทคนิค OCR ด้วย Typhoon OCR

|   def encode\_image\_to\_base64(page) \-\> str:       """แปลงเอกสาร PDF แต่ละหน้าให้เป็นรูปภาพ Base64 เพื่อส่งเข้า API"""       pix \= page.get\_pixmap(matrix\=fitz.Matrix(2.0, 2.0))       img\_bytes \= pix.tobytes("jpeg")       return base64.b64encode(img\_bytes).decode("utf-8")    def ocr\_constitution(meta: dict, skip\_existing: bool \= True):       """ฟังก์ชันหลักในการจัดการไฟล์ภาพ PDF ดึงรูปทีละหน้าส่งเข้า Typhoon OCR"""       cid \= meta\["id"\]       pdf\_path \= PDF\_DIR / meta\["filename"\]             doc \= fitz.open(pdf\_path)       pages\_data \= \[\]        \# วนลูปอ่านข้อมูลทุกหน้าใน PDF       for page\_num in range(doc.page\_count):           page \= doc\[page\_num\]           base64\_image \= encode\_image\_to\_base64(page)                     \# โครงสร้าง Payload ที่จะส่งไปให้ Typhoon V1.5 Vision           payload \= {               "model": "typhoon-v1.5x-70b-vision-instruct",               "messages": \[                   {"role": "user",                    "content": \[                        {"type": "text", "text": "Extract all text from this image."},                        {"type": "image\_url", "image\_url": {"url": f"data:image/jpeg;base64,{base64\_image}"}}                     \]}               \]           }                     \# ส่ง HTTP POST Request           response \= requests.post("https://api.opentyphoon.ai/v1/chat/completions", headers\=headers, json\=payload)           extracted\_text \= response.json()\['choices'\]\[0\]\['message'\]\['content'\]                     pages\_data.append({"page\_num": page\_num \+ 1, "text": extracted\_text})                 \# นำ text ทุกหน้ามารวมกันเป็น full\_text และบันทึกเป็น JSON       \# ... |  |  |
| :---- | ----- | ----- |
|  |  |  |
|  |  |  |

**คำอธิบายโค้ด:** ผู้จัดทำได้สร้างฟังก์ชัน `ocr_constitution` เพื่อรับค่า Metadata ของแต่ละเอกสาร โดยมีกระบวนการทำงานดังนี้:

* ใช้ไลบรารี fitz (PyMuPDF) เปิดไฟล์ PDF แล้วแปลงแต่ละหน้า (Page) ให้กลายเป็นรูปภาพ  
* สร้างฟังก์ชัน `encode_image_to_base64` เพื่อแปลงรูปภาพให้อยู่ในฟอร์แมต Base64  
* วนลูป (Loop) ส่งรูปภาพ Base64 เข้าไปยัง API ของ Typhoon พร้อมคำสั่ง Prompt "Extract all text from this image."  
* รวบรวมข้อความ (Text) ที่ API ตอบกลับมาในรูปแบบ JSON เก็บไว้ในตัวแปร `pages_data`

2. **สำหรับข้อมูลกลุ่ม พ.ศ. 2550–2564 (Text PDF)**: เอกสารกลุ่มนี้เป็น PDF ที่สร้างจากคอมพิวเตอร์และมีข้อความฝังอยู่ (Text PDF) จึงสามารถใช้ไลบรารีสกัดข้อความได้โดยตรง โดยผู้จัดทำสร้างฟังก์ชัน `_extract_text_smart` เพื่อจัดการ:

**ตาราง 2** โค้ดสำหรับการสกัดตัวอักษรด้วยเทคนิคดึงข้อความดิจิทัลโดยตรง

|   def \_extract\_text\_smart(pdf\_path: Path):       """       ฟังก์ชันดึงข้อความจาก PDF อัจฉริยะ:       ลองใช้ PyMuPDF ก่อน ถ้าดึงข้อความได้น้อยกว่ากำหนด จะสลับไปใช้ pdfplumber อัตโนมัติ       """       try:           import fitz           doc \= fitz.open(str(pdf\_path))           \# ดึงข้อความทีละหน้า           pages \= \[{"page\_num": i \+ 1, "text": page.get\_text("text")} for i, page in enumerate(doc)\]           doc.close()                     \# ถ้าดึงข้อความรวมกันได้เกิน 500 ตัวอักษร ถือว่าสำเร็จ           if sum(len(p.get("text", "")) for p in pages) \> 500:               return pages, "pymupdf"       except Exception:           pass        \# Fallback ไปใช้ pdfplumber ถ้าวิธีแรกไม่สำเร็จ       import pdfplumber       with pdfplumber.open(str(pdf\_path)) as pdf:           pages \= \[{"page\_num": i \+ 1, "text": (p.extract\_text() or "")} for i, p in enumerate(pdf.pages)\]       return pages, "pdfplumber" |  |  |
| :---- | ----- | ----- |
|  |  |  |
|  |  |  |

**คำอธิบายโค้ด:** ผู้จัดทำได้สร้างฟังก์ชัน `_extract_text_smart` เพื่อรับค่า Metadata ของแต่ละเอกสารที่เป็นรูปแบบ Text PDF โดยมีกระบวนการทำงานดังนี้:

* ใช้ไลบรารี PyMuPDF (fitz) เป็นตัวดึงข้อความหลัก เนื่องจากมีความเร็วสูง  
* หากพบปัญหาในการดึงข้อความ (เช่น ข้อความได้ค่าน้อยกว่า 500 ตัวอักษร) ระบบจะสลับไปใช้ไลบรารี pdfplumber เป็นตัวสำรอง (Fallback method) อัตโนมัติ เพื่อรักษาความสมบูรณ์ของข้อมูลให้ได้มากที่สุด

## **3.2 การจัดการและทำความสะอาดข้อมูลก่อนนำไปใช้ (Cleaning & Structuring)**

ในการดำเนินการพัฒนาโครงงานได้มีการใช้งานเครื่องมือฮาร์ดแวร์ต่าง ๆ ดังตารางที่ 2 ข้อมูลที่สกัดออกมาทั้งจาก OCR และ Text Extraction ถูกนำเข้ากระบวนการทำความสะอาดข้อมูล (Data Cleaning Pipeline) เพื่อลดสัญญาณรบกวน (Noise) และแก้ไขข้อผิดพลาดทางภาษา ผ่าน 4 ฟังก์ชันย่อย และรวบรวมด้วยฟังก์ชันหลัก `extract_constitution` ดังนี้:

1. **การแปลงอักขระ (Normalization)**: ผู้จัดทำใช้ฟังก์ชัน `_fix_pua` เพื่อแมป (Map) รหัสอักษรเก่าที่อยู่ในช่วง F700-F71A ให้กลับมาเป็น Unicode ตามมาตรฐาน และฟังก์ชัน `_normalize` ร่วมกับไลบรารี `unicodedata` เพื่อปรับอักขระให้เป็น NFC Form และลบอักขระควบคุม (Control Characters) ที่ซ่อนอยู่  
2. **การซ่อมแซมคำผิดด้วย Regular Expression (\_fix\_sara\_am)**: เนื่องจากในเอกสาร Text PDF บางฉบับ มีการเข้ารหัสตัว "สระอำ" ผิดพลาด โดยถูกตัดแบ่งเป็นเว้นวรรคและสระอา (เช่น คำว่า   
   "จ านวน") ผู้จัดทำจึงสร้างฟังก์ชัน `_fix_sara_am` เพื่อใช้ RegEx ตรวจจับพยัญชนะที่ตามด้วยเว้นวรรคและสระอา แล้วแทนที่ให้กลับเป็นสระอำ (ำ) แบบอัตโนมัติ  
3. **การกำจัดส่วนเกินของราชกิจจานุเบกษา (\_remove\_headers)**: เอกสารแต่ละหน้ามักมีข้อความส่วนหัวและเลขหน้าของราชกิจจานุเบกษาปรากฏอยู่ ซึ่งไม่เกี่ยวกับเนื้อหารัฐธรรมนูญ ผู้จัดทำจึงสร้างฟังก์ชัน `_remove_headers` ที่ใช้ RegEx กวาดหาแพทเทิร์นดังกล่าวและลบทิ้ง

**ตาราง 3** โค้ดสำหรับ Data Cleaning Pipeline

|   import re   import unicodedata    def \_fix\_pua(text: str) \-\> str:       """แปลงรหัสอักษรเก่า (PUA) จากฟอนต์เช่น AngsanaUPC ให้กลับเป็น Unicode ปกติ"""       if not text: return ""       pua\_map \= {           0xF700: 0x0E31, 0xF701: 0x0E34, 0xF702: 0x0E35, 0xF703: 0x0E36, 0xF704: 0x0E37,           0xF705: 0x0E48, 0xF706: 0x0E49, 0xF707: 0x0E4A, 0xF708: 0x0E4B, 0xF709: 0x0E4C,           \# ... (แมปช่วง F700-F71A ไปหา 0E31-0E4C) ...       }       return text.translate(pua\_map)    def \_normalize(text: str) \-\> str:       """จัดการทำ Normalization รูปแบบ NFC และลบช่องว่างส่วนเกิน"""       if not text: return ""       text \= unicodedata.normalize("NFC", text)       text \= re.sub(r"\[\\x00\-\\x08\\x0b\\x0c\\x0e\-\\x1f\]", "", text) \# ลบตัวควบคุม       text \= re.sub(r"\[ \\t\]\+", " ", text) \# ยุบช่องว่างให้เหลือ 1 เคาะ       return text.strip()    def \_fix\_sara\_am(text: str) \-\> str:       """แก้ปัญหาสระอำแยกส่วน (เช่น 'จ านวน' \-\> 'จำนวน')"""       SARA\_AM\_PATTERN \= re.compile('(\[ก-ฮ\]\[็-๋\]?) (า)')       return SARA\_AM\_PATTERN.sub(lambda m: m.group(1) \+ 'ำ', text)    def \_remove\_headers(text: str) \-\> str:       """ตัดข้อความส่วนหัว/ส่วนท้ายของเอกสารราชกิจจานุเบกษาออก"""       patterns \= \[           r"\\u0E2B\\u0E19\\u0E49\\u0E32\\s\*\\d\+\\s\*\\u0E40\\u0E25\\u0E48\\u0E21\\s\*\\d\+.\*?\\u0E23\\u0E32\\u0E0A\\u0E01\\u0E34\\u0E08\\u0E08\\u0E32\\u0E19\\u0E38\\u0E40\\u0E1A\\u0E01\\u0E29\\u0E32\[^\\n\]\*",           r"^\\s\*\-\\s\*\\d\+\\s\*\-\\s\*$",           r"^\\s\*\\d\+\\s\*$",       \]       for pattern in patterns:           text \= re.sub(pattern, "", text, flags\=re.MULTILINE | re.IGNORECASE)       return text |  |  |
| :---- | ----- | ----- |
|  |  |  |
|  |  |  |

4. **การบันทึกข้อมูลแบบมีโครงสร้าง (JSON Structuring):** กระบวนการทำงานทั้งหมดจะถูกประมวลผลผ่านฟังก์ชันรวม `extract_constitution` เพื่อทำการนำข้อมูลแต่ละหน้า (Page) มาวนลูปทำความสะอาดทีละฟังก์ชัน แล้วรวบรวมเก็บเป็น Dictionary เดี่ยว และบันทึกผลลัพธ์เป็นไฟล์ .json ตามโครงสร้างที่ออกแบบไว้ในบทที่ 2.3 ทำให้ได้ไฟล์ที่มีโครงสร้างมาตรฐานเดียวกัน พร้อมส่งต่อให้ขั้นตอนการสร้างแบบจำลอง (Modeling) ทันที

**ตาราง 4** โค้ดสำหรับ Data Pipeline Structuring

|   def extract\_constitution(meta: dict, skip\_existing: bool \= True):       """ฟังก์ชันไปป์ไลน์หลัก รวบรวมการสกัดข้อความ การทำความสะอาด และจัดโครงสร้าง"""       pdf\_path \= PDF\_DIR / meta\["filename"\]             \# 1\. ดึงข้อความจากไฟล์       pages\_data, method \= \_extract\_text\_smart(pdf\_path)        \# 2\. นำข้อความแต่ละหน้าผ่านกระบวนการทำความสะอาด (Cleaning Pipeline)       for p in pages\_data:           text \= \_fix\_pua(p.get("text", ""))           text \= \_normalize(text)           text \= \_fix\_sara\_am(text)           text \= \_remove\_headers(text)           p\["text"\] \= text        \# 3\. นำข้อความทุกหน้ามาต่อรวมกัน       full\_text \= \_normalize("\\n\\n".join(p\["text"\] for p in pages\_data if p.get("text")))        \# 4\. จัดโครงสร้างข้อมูล Metadata ให้อยู่ในฟอร์แมต JSON Schema       result \= {           "id":                meta\["id"\],           "year\_th":           meta\["year\_th"\],           "name\_short":        meta\["name\_short"\],           "source\_type":       "text\_pdf",           "processing\_method": method,           "total\_pages":       len(pages\_data),           "pages":             pages\_data,           "full\_text":         full\_text,           "metadata": {               "total\_chars":        len(full\_text),               "total\_words\_approx": len(full\_text.split()),           },       }       return result |  |  |
| :---- | ----- | ----- |
|  |  |  |
|  |  |  |

## **3.3 การจัดโครงสร้างข้อมูลเชิงลึก  (Deep Structure Parsing)**

	หลังจากผ่านกระบวนการ Extraction และ Clean ข้อมูลใน 3.1 และ 3.2 มาแล้ว ข้อมูลที่ได้ยังอยู่ในรูปแบบ raw text ต่อหน้า ซึ่งยังไม่สามารถนำไปวิเคราะห์เชิงโครงสร้างได้โดยตรง คณะผู้จัดทำจึงพัฒนา Post-Processor สำหรับแปลงข้อมูลให้มีโครงสร้างแบบ Hierarchical ตาม 3 ระดับของรัฐธรรมนูญไทย ได้แก่ หมวด (Chapter), ส่วนที่ (Part), และ มาตรา (Section) แล้ว export ออกมาในรูปแบบ JSON และ CSV

1. **การ parse โครงสร้างหมวด ส่วนที่ และมาตรา**

	ฟังก์ชัน `_split_by_boundary` มีหน้าที่ตรวจจับขอบเขตของแต่ละหมวดด้วย Regular Expression โดยรองรับทั้งรูปแบบ หมวดที่ N, บทที่ N และหมวดพิเศษ เช่น บททั่วไป และ บทเฉพาะกาล จากนั้นฟังก์ชัน `_parse_parts_from_segment` ใช้สำหรับตรวจว่าในหมวดนั้นมี ส่วนที่ ซ้อนอยู่ด้วยหรือไม่ และฟังก์ชัน `_parse_sections_from_segment` ใช้การ slice ตาม position ของคำว่า มาตรา N แทนการใช้ Regex แบบ non-greedy เพื่อให้ข้อมูลในแต่ละมาตราครบถ้วนไม่ถูกตัดกลางคัน

**ตาราง 5** ฟังก์ชัน \_parse\_sections\_from\_segment และ \_merge\_cross\_chapter\_duplicates

| def \_parse\_sections\_from\_segment(text: str) \-\> List\[Any\]:     """ ค้นหาและแยกเนื้อหาของแต่ละมาตราโดยใช้ตำแหน่งเริ่มต้นของ มาตรา N ใช้วิธีตัดข้อความ (Slice) ตามตำแหน่งที่พบเพื่อให้อ่านข้อมูลได้ครบถ้วนและแม่นยำกว่าการใช้ Regex แบบปกติ """     matches \= list(\_RE\_SECTION\_START.finditer(text))     raw\_sections: List\[Any\] \= \[\]     for i, m in enumerate(matches):         sec\_num \= int(m.group(1))         content\_start \= m.end()         content\_end \= matches\[i \+ 1\].start() if i \+ 1 \< len(matches) else len(text)                 \# ทำความสะอาดข้อความโดยการยุบช่องว่างที่ซ้ำซ้อนให้เหลือเพียงช่องเดียว         sec\_text \= re.sub(r'\\s\+', ' ', text\[content\_start:content\_end\]).strip()         if sec\_text:             raw\_sections.append(Section(section\_number\=sec\_num, text\=sec\_text))     \# รวมมาตราที่มีเลขซ้ำกัน (จัดการกรณีที่ผลจาก OCR มีหัวข้อแทรกกลางเนื้อหามาตรา)     merged: List\[Any\] \= \[\]     for sec in raw\_sections:         if merged and merged\[\-1\].section\_number \== sec.section\_number:             \# รวมเนื้อหาเข้ากับมาตราก่อนหน้า             merged\[\-1\] \= Section(                 section\_number\=sec.section\_number,                 text\=merged\[\-1\].text \+ ' ' \+ sec.text             )         else:             merged.append(sec)                 return merged  def \_merge\_cross\_chapter\_duplicates(chapters: List\[Any\]) \-\> List\[Any\]:     """ รวมเนื้อหาของมาตราที่มีเลขซ้ำกันข้ามบท (Chapter) โดยข้อมูลที่ซ้ำจะถูกนำไปต่อท้ายเนื้อหาในบทแรกที่พบมาตราเลขนั้นๆ """     seen: Dict\[int, int\] \= {}  \# เก็บค่า section\_number \-\> index ของบทที่พบครั้งแรก         for ci, ch in enumerate(chapters):         new\_secs \= \[\]         for sec in ch.sections:             n \= sec.section\_number             if n in seen:                 \# หากเคยพบมาตรานี้แล้วในบทก่อนหน้า ให้นำเนื้อหาไปรวมกัน                 orig\_chapter\_index \= seen\[n\]                 orig\_secs \= chapters\[orig\_chapter\_index\].sections                 for si, s in enumerate(orig\_secs):                     if s.section\_number \== n:                         orig\_secs\[si\] \= Section(                             section\_number\=n,                             text\=s.text \+ ' ' \+ sec.text                         )                         break             else:                 \# หากยังไม่เคยพบ ให้บันทึก index ของบทปัจจุบันไว้                 seen\[n\] \= ci                 new\_secs.append(sec)                 \# อัปเดตรายการมาตราในบทปัจจุบัน (ตัดมาตราที่ถูกย้ายไปรวมที่อื่นออก)         ch.sections \= new\_secs      return chapters |
| :---- |

### 

2. ### **การตรวจจับประเภทฉบับ (Original / Amendment)**

รัฐธรรมนูญบางฉบับที่มีการประกาศออกมา เป็นฉบับแก้ไขเพิ่มเติม ไม่ใช่ฉบับประกาศใหม่ ดังนั้นฟังก์ชัน `_detect_constitution_type` ไว้ตรวจสอบ keyword เช่น แก้ไขเพิ่มเติม หรือ amendment ใน `name_short` และเนื้อหาต้น แล้วส่งคืนค่า `constitution_type` และ `amends_year` เพื่อให้การวิเคราะห์เปรียบเทียบสามารถ reference กลับไปยังฉบับหลักได้ถูกต้อง

**ตาราง 6** ฟังก์ชัน \_detect\_constitution\_type 

| \# คำสำคัญสำหรับตรวจสอบว่าเป็นฉบับแก้ไขเพิ่มเติมหรือไม่ \_AMENDMENT\_KEYWORDS \= \[     'แก้ไขเพิ่มเติม', 'ฉบับแก้ไข', 'แก้ไข พ.ศ.', 'amendment', \] def \_detect\_constitution\_type(raw\_data: Dict) \-\> Tuple\[str, Optional\[int\]\]:     """ ตรวจสอบประเภทของรัฐธรรมนูญว่าเป็นฉบับหลัก (Original) หรือฉบับแก้ไขเพิ่มเติม (Amendment)     พร้อมทั้งระบุปีที่ได้รับการแก้ไขหากเป็นฉบับแก้ไขเพิ่มเติม """     \# รวมชื่อย่อและเนื้อหา 500 ตัวอักษรแรกเพื่อใช้ในการค้นหาคำสำคัญ     name \= raw\_data.get('name\_short', '') \+ ' ' \+ raw\_data.get('full\_text', '')\[:500\]         \# ตรวจสอบว่ามีคำสำคัญที่ระบุว่าเป็นฉบับแก้ไขเพิ่มเติมหรือไม่     is\_amendment \= any(kw in name for kw in \_AMENDMENT\_KEYWORDS)         if is\_amendment:         \# ค้นหาปี พ.ศ. ที่ระบุในบริบทของการแก้ไขเพิ่มเติม         year\_match \= re.search(r'แก้ไข.\*?(\\d{4})', name)         amends\_year \= int(year\_match.group(1)) if year\_match else None         return 'amendment', amends\_year      return 'original', None |
| :---- |

3. **การ Export JSON และ CSV** 

ฟังก์ชัน \_iter\_all\_sections เป็น Generator ที่ traverse โครงสร้าง chapters ไป parts ไป sections แล้ว yield dict row ออกมาทีละ 1 มาตรา ซึ่งนำไปใช้ทั้งใน การบันทึก JSON แบบ nested และ CSV แบบ flat ทำให้ code ไม่ซ้ำซ้อน

**ตาราง 7** ฟังก์ชัน \_iter\_all\_sections สำหรับ Export 

| def \_iter\_all\_sections(data: Dict\[str, Any\]) \-\> Generator\[Dict\[str, Any\], None, None\]:     """ Generator สำหรับวนลูปข้อมูลมาตราทั้งหมด โดยคืนค่าเป็น Dictionary หนึ่งแถวต่อหนึ่งมาตรา     รองรับโครงสร้างข้อมูลแบบลำดับชั้น: หมวด (Chapter) \-\> ส่วน (Part) \-\> มาตรา (Section) """     \# กำหนดข้อมูลพื้นฐานที่ใช้ร่วมกันในทุกมาตรา     base \= {         'constitution\_id': data\['id'\],         'year\_th': data\['year\_th'\],         'year\_ce': data\['year\_ce'\],         'constitution\_type': data.get('constitution\_type'),         'amends\_year': data.get('amends\_year', ''),         'era': data.get('era', ''),         'regime\_type': data.get('regime\_type', ''),     }     for chap in data\['chapters'\]:         \# สร้าง Context ของหมวด (Chapter)         chap\_ctx \= {             \*\*base,             'chapter\_number': chap\['chapter\_number'\],             'chapter\_title': chap\['chapter\_title'\]         }         \# วนลูปมาตราที่สังกัดอยู่ในหมวดโดยตรง (กรณีที่ไม่มีการแบ่งเป็น "ส่วนที่")         for sec in chap.get('sections', \[\]):             yield {                 \*\*chap\_ctx,                 'part\_number': '',                 'part\_title': '',                 'section\_number': sec\['section\_number'\],                 'section\_text': sec\['text'\]             }         \# วนลูปมาตราที่แบ่งตาม "ส่วนที่" (Part) ภายในหมวดนั้นๆ         for part in chap.get('parts', \[\]):             for sec in part.get('sections', \[\]):                 yield {                     \*\*chap\_ctx,                     'part\_number': part\['part\_number'\],                     'part\_title': part\['part\_title'\],                     'section\_number': sec\['section\_number'\],                     'section\_text': sec\['text'\]                 } |
| :---- |

## 

## **3.4 สรุปผลลัพธ์การเตรียมข้อมูล (Data Preparation Results)**

หลังจากผ่านกระบวนการ Extraction Cleaning และจัดโครงสร้างข้อมูลทั้งหมดแล้ว จะได้ผลลัพธ์เป็นไฟล์ 2 รูปแบบต่อ 1 ฉบับ ได้แก่ Structured JSON และ Flat CSV รวมทั้งสิ้น 38 ฉบับ ครอบคลุมรัฐธรรมนูญและธรรมนูญการปกครองไทยทุกฉบับ

1. ### **โครงสร้าง Structured JSON (structured\_YYYY.json)**

ไฟล์ JSON มีโครงสร้างแบบ Hierarchical 3 ระดับ ได้แก่ ระดับ Root เก็บ metadata ของฉบับ ระดับ chapters เก็บข้อมูลรายหมวด และระดับ sections/parts เก็บรายมาตรา โดยมี field สำคัญดังตารางที่ 8

**ตาราง 8 โครงสร้าง field ใน Structured JSON** 

| Field | Type | ตัวอย่าง | คำอธิบาย | Field |
| :---: | :---: | :---: | :---: | :---: |
| id | string | const\_2475 | unique ID ของฉบับ | id |
| year\_th / year\_ce | int | 2475 / 1932 | ปี พ.ศ. และ ค.ศ. | year\_th / year\_ce |
| constitution\_type | string | original / amendment | ประเภทฉบับ | constitution\_type |
| amends\_year | int | null | 2475 / null | ปีฉบับที่ถูกแก้ไข | amends\_year |
| era / regime\_type | string | early\_democracy | ยุคสมัยและระบอบ | era / regime\_type |
| preamble | string | สมเด็จพระ... | คำปรารภ  (สูงสุด 2,000 chars) | preamble |
| summary.total\_chapters | int | 7 | จำนวนหมวดทั้งหมด | summary.total\_chapters |

### 

### 

2. ### **โครงสร้าง Flat CSV (sections\_YYYY.csv และ all\_sections\_combined.csv)**

ไฟล์ CSV มีรูปแบบ 1 row ต่อ 1 มาตรา เรียงตาม section\_number เหมาะสำหรับการนำไปวิเคราะห์ด้วย โดยไฟล์ all\_sections\_combined.csv จะรวมทุกฉบับไว้ด้วยกัน สำหรับ cross-version analysis

**ตาราง 9 โครงสร้าง column ใน Flat CSV**

| Column | Type | ตัวอย่าง | คำอธิบาย |
| :---- | :---- | :---- | :---- |
| constitution\_id | string | const\_2475 | unique ID ของฉบับ |
| year\_th / year\_ce | int | 2475 / 1932 | ปี พ.ศ. และ ค.ศ. |
| constitution\_type | string | original | original หรือ amendment |
| amends\_year | int | empty | 2475 | ปีฉบับที่แก้ไข (ถ้าเป็น amendment) |
| era / regime\_type | string | early\_democracy | ยุคสมัยและระบอบ |
| chapter\_number | int | 1 | เลขหมวด |
| chapter\_title | string | พระมหากษัตริย์ | ชื่อหมวด |
| part\_number | int | empty | 2 | เลขส่วน (ว่างถ้าไม่มี ส่วนที่) |
| part\_title | string | empty | ส่วนที่ 2 สภาผู้แทน | ชื่อส่วน |
| section\_number | int | 3 | เลขมาตรา |
| section\_text | string | องค์พระมหากษัตริย์... | เนื้อหามาตรา (cleaned) |

3. ### **ผลลัพธ์ภาพรวม**

ตารางที่ 10 แสดงสรุปจำนวนหมวด ส่วน และมาตราของรัฐธรรมนูญไทยฉบับหลักที่ผ่านกระบวนการ Post-Processing เรียบร้อยแล้ว

**ตาราง 10 สรุปผลการจัดโครงสร้างข้อมูลรัฐธรรมนูญฉบับหลัก**

| ปี พ.ศ. | เอกสาร | หมวด | ส่วน | มาตรา | จำนวนคำ (โดยประมาณ) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2475 | Constitution 2475 | 7 | 0 | 68 | 987 |
| 2489 | Constitution 2489 | 9 | 0 | 96 | 2,021 |
| 2492 | Constitution 2492 | 11 | 6 | 223 | 3,238 |
| 2517 | Constitution 2517 | 12 | 4 | 238 | 4,033 |
| 2540 | Constitution 2540 | 15 | 8 | 336 | 7,693 |
| 2550 | Constitution 2550 | 15 | 7 | 309 | 9,367 |
| 2560 | Constitution 2560 | 16 | 10 | 279 | 7,939 |

(รวมทุกฉบับ 38 เอกสาร ได้มาตราทั้งหมดประมาณ 3,200 มาตรา รวมประมาณ 61,301 คำ พร้อม export เป็น all\_sections\_combined.csv สำหรับ cross-version analysis)

# **บทที่ 4 การเตรียมและการจัดการข้อมูล**

---

	Lorem