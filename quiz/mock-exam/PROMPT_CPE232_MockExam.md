# Prompt: สร้างข้อสอบจำลองปลายภาค CPE232 Data Models

> **วิธีใช้:** คัดลอกข้อความตั้งแต่บรรทัด `===== BEGIN PROMPT =====` จนถึง `===== END PROMPT =====` ไปวางใน Claude (หรือ AI ที่ใช้) พร้อมแนบไฟล์อ้างอิงทั้ง 6 ไฟล์ที่ระบุ

---

===== BEGIN PROMPT =====

คุณคือผู้เชี่ยวชาญด้าน Machine Learning และเป็นอาจารย์ผู้ออกข้อสอบรายวิชา **CPE232 Data Models** ของมหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี (KMUTT) ภารกิจของคุณคือสร้าง **ข้อสอบจำลองปลายภาค (Mock Final Exam)** เป็นภาษาไทย ในรูปแบบไฟล์ LaTeX (`.tex`) ที่ compile ได้ด้วย XeLaTeX โดยใช้ฟอนต์ TH Sarabun New

## 1. ไฟล์อ้างอิง (Input Files)

ใช้เนื้อหาจากไฟล์ต่อไปนี้เป็นแหล่งความรู้หลัก:

1. `lectures/DataModels_6_ML_classification.pdf` — Classification (Decision Tree, KNN, Naive Bayes, Logistic Regression, SVM, Random Forest, Confusion Matrix, Accuracy/Precision/Recall/F1)
2. `lectures/DataModels_7_ML_regression.pdf` — Regression (Linear/Polynomial/Decision Tree Regression, MSE/RMSE/MAE, Gradient Descent, R², Ridge/Lasso)
3. `lectures/DataModels_8_ML_ParameterTuning.pdf` — Parameter Tuning (Hyperparameters vs Learnable Params, Overfitting/Underfitting, Cross-Validation, Grid/Random Search, Bayesian Optimization, GD variants, Learning Rate Scheduling, Adam/RMSProp/Adagrad)
4. `lectures/DataModels_9_ML_clustering.pdf` — Clustering (K-Means, WCSS, Elbow Method, Silhouette Score, Hierarchical Agglomerative/Divisive, Dendrogram, Proximity Matrix, DBSCAN, Distance Functions)
5. `quiz/mock-exam/final_dtmodel.pdf` — แนวข้อสอบเก่าที่รุ่นพี่รวบรวม (ใช้เป็น reference สำหรับ pattern คำถามและความยาก)
6. `quiz/mock-exam/CPE232_Final_PracticeCalculation.pdf` — แบบฝึกหัดคำนวณ (ใช้เป็น reference สำหรับข้อคำนวณ)

**Format อ้างอิง:** ใช้รูปแบบ LaTeX ตามไฟล์ `quiz/mock-exam/CPE241_M3_Mock_Exam.tex` (preamble, การจัดหัวข้อ Part, ส่วนเฉลย, ส่วน RECAP, การใช้ `\needspace`, `\blank`, `\ans`, `enumitem`, `multicols`, `tikz` สำหรับ dendrogram/diagram)

## 2. แนวทางการออกข้อสอบ (Exam Guidance — ต้องปฏิบัติตามทุกข้อ)

### 2.1 จากอาจารย์ผู้สอน

- ครอบคลุมทุกหัวข้อหลังสอบกลางภาค (Lecture 6–9 เท่านั้น)
- รูปแบบข้อสอบผสม: **Multiple Choice + Multiple Selection + True/False + Short Answer + Long Answer + Calculation**
- มี Formula Sheet ให้ในห้องสอบ จึง**ไม่ต้องท่องสูตร** แต่ต้องเข้าใจวิธีใช้
- เวลาสอบ **3 ชั่วโมง** สอบ Onsite
- **คะแนนเต็ม 100 คะแนน**

### 2.2 จากแนวรุ่นพี่คนที่ 1

- เน้น**ทฤษฎีแบบตะโกน** ต้องเตรียมนิยามให้แม่น
- ต้องอธิบายได้ว่า**ทำไมตัดสินใจแบบนี้** (justify การเลือกใช้อัลกอริทึม/hyperparameter)
- มีโจทย์**ตีความ data** ว่าผลลัพธ์แบบนี้ตีความว่าอย่างไรได้บ้าง (ใช้ทักษะเขียนเรียงความ)
- **ต้องมีโจทย์ Agglomerative Hierarchical Clustering 1 ข้อ** พร้อมให้วาด **Dendrogram** และ **Nested Cluster Diagram**

### 2.3 จากแนวรุ่นพี่คนที่ 2

- มีโจทย์ให้**เขียนนิยามคำศัพท์จาก Lecture 6–9 รวมประมาณ 10 คำ** (เช่น Clustering, Feature Extraction, Overfitting, Cross-Validation, Centroid, Entropy, Information Gain, Hyperparameter, Confusion Matrix, Silhouette Score เป็นต้น)
- **โจทย์ Entropy** (ถ้ามี) — ค่า log ต้องเป็นเลขที่**ลงตัว** (เช่น log₂(1/2) = -1, log₂(1/4) = -2, log₂(1/8) = -3) **หรือ**ให้ค่าคงที่ log แต่ละค่ามาตอนเริ่มโจทย์ (เช่น "กำหนดให้ log₂(3) ≈ 1.585, log₂(5) ≈ 2.322")

### 2.4 จากแนวรุ่นพี่คนที่ 3 (สำคัญที่สุด — ระบุชัดเจน)

**"ปลายภาคเขียน 90%"** — ข้อสอบเน้น **ข้อเขียน + คำนวณ** เป็นหลัก ส่วน MCQ มีเพียง 10% เท่านั้น หัวข้อที่ออกแน่ ๆ มีดังนี้:

1. **4 Model แต่ละอันใช้เพื่ออะไร สำคัญอย่างไร** — ต้องเปรียบเทียบและอธิบาย use case ของ 4 model สำคัญในเนื้อหา เช่น
   - **Classification 4 ตัวหลัก:** Decision Tree, KNN, Naive Bayes, Random Forest (หรือเลือก Logistic Regression / SVM ก็ได้)
   - **หรือ 4 หัวข้อใหญ่ใน Lecture 6–9:** Classification / Regression / Parameter Tuning / Clustering
2. **วิธีคำนวณ Entropy และ Information Gain** — ต้องแสดงวิธีทำทุกขั้น
3. **Types of Cross-Validation แต่ละแบบ** — k-Fold, Stratified k-Fold, Leave-One-Out (LOO-CV), Time Series CV — บอก concept, ข้อดี-ข้อจำกัด, และเหมาะกับ dataset แบบใด
4. **วิธีคำนวณ Confusion Matrix** — Accuracy, Precision, Recall, F1-Score, Specificity
5. **วิธีคำนวณ Regression** — MSE, RMSE, MAE, R², และอาจรวม Gradient Descent update
6. **วิธีทำ Hierarchical Agglomerative Clustering** — Proximity Matrix → Merge → Dendrogram → Nested Clusters
7. **ทฤษฎีแต่ละเรื่อง** — ต้องจำได้ทั้งหมด ไม่มีให้เปิดสรุป (มีแต่ Formula Sheet)

> **ข้อสรุป:** เนื่องจากเป็น "เขียน 90%" จึงต้องจัดสรรคะแนนให้ **Calculation + Long/Short Answer + Definition ≥ 90 คะแนน** และ **MCQ ≤ 10 คะแนน** เท่านั้น

## 3. โครงสร้างข้อสอบที่ต้องสร้าง (100 คะแนน — เน้นเขียน 90%)

จัดสรรคะแนนและส่วนต่าง ๆ ดังนี้:

### Part 1: Multiple Choice + Multiple Selection + True/False (10 คะแนน — สัดส่วน MCQ 10%)

- **1.1 Multiple Choice** (5 คะแนน — 5 ข้อ ข้อละ 1 คะแนน) ครอบคลุม Lecture 6–9 ในสัดส่วนใกล้เคียงกัน เน้น concept ไม่ใช่จำชื่อ
- **1.2 Multiple Selection** (3 คะแนน — 3 ข้อ ข้อละ 1 คะแนน) เลือกได้มากกว่า 1 ข้อ
- **1.3 True/False** (2 คะแนน — 4 ข้อ ข้อละ 0.5 คะแนน) จริง/เท็จ ไม่ต้องอธิบาย

### Part 2: Definition (10 คะแนน — 10 คำ ข้อละ 1 คะแนน)

เขียนนิยามคำศัพท์ 10 คำจาก Lecture 6–9 (ภาษาไทยหรืออังกฤษได้) คัดเลือกคำให้ครอบคลุมทั้ง 4 บท ตัวอย่างชุดคำที่ต้องเลือก:

- **Lecture 6:** Entropy, Information Gain, Confusion Matrix, F1-Score, Bagging, Boosting
- **Lecture 7:** Coefficient of Determination (R²), Gradient Descent, Regularization, Polynomial Regression
- **Lecture 8:** Hyperparameter, k-Fold Cross-Validation, Overfitting, Underfitting, Grid Search
- **Lecture 9:** Centroid, Silhouette Score, Dendrogram, DBSCAN, Proximity Matrix, WCSS

เว้นที่ตอบ ~2.5 ซม. ต่อข้อ

### Part 3: Short Answer & Data Interpretation (15 คะแนน — 5 ข้อ ข้อละ 3 คะแนน)

ตอบสั้น 2–4 บรรทัด เน้น "**ทำไม**" และ "**ตีความ**" ตัวอย่างคำถาม:

- "เพราะเหตุใดจึงเลือกใช้ Random Forest แทน Decision Tree เดี่ยว?"
- "ถ้า Training Accuracy = 98%, Test Accuracy = 65% ปัญหาคืออะไรและแก้อย่างไร?"
- "Confusion Matrix นี้บอกอะไรเกี่ยวกับ classifier?" (กำหนด TP/FP/FN/TN มาให้)
- "Silhouette Score = 0.15 บอกอะไรเกี่ยวกับคุณภาพการ cluster และควรทำอย่างไรต่อ?"
- "Gradient Descent ติด Local Minimum ตอนไหน และแก้อย่างไรด้วย optimizer สมัยใหม่?"

### Part 4: Long Answer / Essay (20 คะแนน) — ตอบยาว เน้นเขียนเรียงความ

#### 4.1 เปรียบเทียบ 4 Model (10 คะแนน — 1 ข้อ)

- ให้เปรียบเทียบ **4 Model ใน Classification** (Decision Tree, KNN, Naive Bayes, Random Forest) ครอบคลุม:
  - หลักการทำงานสั้น ๆ
  - ข้อดี / ข้อจำกัด
  - **ใช้เพื่อ use case แบบใด สำคัญอย่างไร**
  - เลือกใช้แบบใดเมื่อ dataset มีลักษณะแบบนี้... (มีโจทย์สถานการณ์)
- ตอบยาว ~12–15 บรรทัด อาจให้เขียนเป็นตารางหรือเรียงความก็ได้

#### 4.2 Types of Cross-Validation (10 คะแนน — 1 ข้อ)

- อธิบาย Cross-Validation แต่ละแบบ: **k-Fold, Stratified k-Fold, Leave-One-Out (LOO-CV), Time Series CV**
- บอก concept, ข้อดี, ข้อจำกัด, และเหมาะกับ dataset แบบใด
- มีโจทย์สถานการณ์ให้เลือกใช้: "Dataset เป็น stock price 5 ปี ควรใช้ CV แบบใด ทำไม?"
- ตอบยาว ~12–15 บรรทัด

### Part 5: Calculation (45 คะแนน) — คะแนนหลักของข้อสอบ

#### 5.1 Decision Tree — Entropy & Information Gain (10 คะแนน)

- ให้ตาราง data ขนาด 6–10 แถว ที่ตัวเลขแบ่งลงตัว เช่น สัดส่วน 4/4, 2/2/4, 3/3 เพื่อให้ log₂ ออกเป็นจำนวนเต็มหรือเศษส่วนสวย ๆ
- **หรือ** ระบุที่ส่วนหัวโจทย์ว่า "กำหนดให้ log₂(3) ≈ 1.585, log₂(5) ≈ 2.322, log₂(7) ≈ 2.807"
- คำนวณ:
  - Entropy(S) ของทั้ง dataset
  - Information Gain ของแต่ละ attribute (3–4 attribute)
  - เลือก root node และอธิบายเหตุผล
- แสดงวิธีทำทุกขั้น

#### 5.2 Confusion Matrix Metrics (8 คะแนน)

- ให้ confusion matrix 2×2 (หรือ multi-class 3×3) มาเป็นโจทย์
- คำนวณ:
  - Accuracy
  - Precision (ต่อ class)
  - Recall (ต่อ class)
  - F1-Score
  - Specificity (ถ้าเป็น binary)
- ตีความว่า class ไหนมีปัญหา และเสนอวิธีแก้ (เช่น เพิ่ม training data, ปรับ threshold, oversampling)

#### 5.3 Regression — MSE/RMSE/MAE & R² (10 คะแนน)

- ให้คู่ (y_actual, y_predicted) 4–5 จุด
- คำนวณ:
  - MSE, RMSE, MAE
  - SSE และ SS_total
  - R² (Coefficient of Determination)
- อาจมีข้อย่อยถาม Gradient Descent: ให้ θ ปัจจุบัน, learning rate, gradient → คำนวณ θ ใหม่หลัง update 1 step
- ตีความว่า model fit ดีหรือไม่

#### 5.4 K-Means Clustering (5 คะแนน)

- ให้จุดข้อมูล 2D ~6 จุด พร้อม initial centroids 2 ตัว
- คำนวณ Euclidean Distance, จัด cluster, update centroid ทำ 1–2 iterations
- บอกว่า converge หรือยัง พร้อมเหตุผล

#### 5.5 Hierarchical Agglomerative Clustering + Dendrogram + Nested Clusters (12 คะแนน) — ต้องมี (รุ่นพี่ 1 + 3 ย้ำ)

- ให้จุดข้อมูล 4–5 จุด **หรือ** Proximity Matrix มาตรง ๆ
- ใช้ **Complete Linkage** (หรือ Single/Average — ระบุชัด)
- ทำ merge ทีละขั้นจนเหลือ 1 cluster:
  - แสดง Proximity Matrix ทุก iteration
  - ระบุคู่ที่ merge และระยะทาง
- **วาด Dendrogram** ด้วย TikZ พร้อมระบุระดับ distance ที่ merge แต่ละครั้ง (แกน y = distance)
- **วาด Nested Cluster Diagram** (วงล้อมจุดที่อยู่ cluster เดียวกัน)
- ตอบคำถาม: "ถ้าตัด dendrogram ที่ระดับ d = X จะได้กี่ cluster และแต่ละ cluster ประกอบด้วยจุดอะไรบ้าง?"

> **หมายเหตุ:** รวม Part 5 = 10 + 8 + 10 + 5 + 12 = **45 คะแนน** (45% ของข้อสอบเป็น calculation ตามแนวรุ่นพี่ 3 ที่บอกว่าเขียน 90%)
>
> **สรุปสัดส่วนคะแนนรวม:**
> - Part 1 (MCQ/Multi/T-F): 10 คะแนน — **10%**
> - Part 2 (Definition): 10 คะแนน — เขียน
> - Part 3 (Short Answer): 15 คะแนน — เขียน
> - Part 4 (Long/Essay): 20 คะแนน — เขียน
> - Part 5 (Calculation): 45 คะแนน — เขียน/คำนวณ
> - **รวมเขียน + คำนวณ = 90%** ตรงตามแนวรุ่นพี่คนที่ 3

## 4. รูปแบบไฟล์ LaTeX (Output Format)

### 4.1 Preamble (ใช้ตามไฟล์ตัวอย่าง CPE241_M3_Mock_Exam.tex)

```latex
\documentclass[a4paper,12pt]{article}
\usepackage{fontspec}
\usepackage{xunicode}
\usepackage{xltxtra}
\usepackage[margin=2.5cm]{geometry}
\usepackage{enumitem}
\usepackage[table]{xcolor}
\usepackage{graphicx}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows, positioning, fit, calc, trees}
\usepackage{float}
\usepackage[normalem]{ulem}
\usepackage{needspace}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{multicol}
\usepackage{array}

\setmainfont{TH Sarabun New}
\setmonofont{Courier New}

\XeTeXlinebreaklocale "th"
\XeTeXlinebreakskip = 0pt plus 1pt
\linespread{1.15}

\newcommand{\blank}[1]{\fbox{\rule{0pt}{1.1em}\hspace{#1}}}
\newcommand{\ans}[1]{\textbf{#1}}
```

### 4.2 หัวเอกสาร

```
\textbf{\Large CPE 232 Data Models}
\textbf{Mock Final Exam (ข้อสอบจำลองปลายภาค)}
เวลาสอบ: 3 ชั่วโมง | คะแนนเต็ม: 100 คะแนน | สอบ Onsite
```

ตามด้วยประกาศและขอบเขตข้อสอบ และระบุ:

- "**มี Formula Sheet ให้ในห้องสอบ — ไม่ต้องท่องสูตร**"
- "**ข้อสอบส่วนใหญ่เป็นข้อเขียน (~90%) MCQ มีเพียงเล็กน้อย**"

### 4.3 ลำดับโครงสร้างไฟล์

1. หัวเอกสาร + ประกาศ + ภาพรวมคะแนน
2. Part 1: Multiple Choice + Multi-Select + True/False
3. Part 2: Definition (10 คำ)
4. Part 3: Short Answer & Data Interpretation
5. Part 4: Long Answer / Essay (4-Model + Cross-Validation)
6. Part 5: Calculation (5.1–5.5)
7. `\newpage` → **เฉลยและแนวคิด (Answer Key)** — แสดงคำตอบและวิธีทำของทุก Part อย่างละเอียด
8. `\newpage` → **Formula Sheet** — สูตรทั้งหมดของ Lecture 6–9 (เลียนแบบ Formula Sheet ที่อาจารย์จะให้ในห้องสอบ) แบ่งเป็น 4 ส่วนตาม Lecture
9. `\newpage` → **RECAP สำหรับอ่านก่อนสอบ** — สรุป pattern จำสอบของแต่ละ Lecture แบ่งเป็น:
   - **RECAP 1: Classification** (4 Model หลัก + Confusion Matrix + Metrics)
   - **RECAP 2: Regression** (Loss functions + GD + R² + Ridge/Lasso)
   - **RECAP 3: Parameter Tuning** (Hyperparameter + Overfitting + 4 Types of CV + Grid/Random Search + Optimizer)
   - **RECAP 4: Clustering** (K-Means + Hierarchical Agglomerative + DBSCAN + Distance functions + Silhouette)

### 4.4 รายละเอียดเชิงเทคนิคของไฟล์

- ใช้ `\needspace{6\baselineskip}` ก่อนเริ่มข้อใหม่ทุกข้อ MCQ และก่อนข้อ Calculation
- ใช้ `\vspace{...}` กำหนดที่ว่างให้นักศึกษาเขียนตอบ:
  - Definition ~2.5 cm
  - Short Answer ~3 cm
  - Long Answer ~8 cm
  - Calculation ~6–10 cm (ตามความยาก)
- ใช้ `\begin{enumerate}[label=\textbf{\arabic*.}]` สำหรับ numbering ข้อหลัก
- ใช้ `\begin{enumerate}[label=\alph*.]` สำหรับตัวเลือก a–d
- สูตรคณิตศาสตร์ใช้ `\[ ... \]` หรือ `\begin{aligned}`
- ตารางใช้ `\rowcolor{cyan!15}` สำหรับ header
- **Dendrogram** ใช้ TikZ — วาดแบบ binary tree แนวตั้ง พร้อมแกน y แสดงระยะทาง
- **Nested Cluster Diagram** ใช้ TikZ — วาดวงล้อมจุด data points
- **Confusion Matrix** วาดเป็นตาราง 2×2 หรือ 3×3 มี header "Predicted" และ "Actual"
- ส่วนเฉลย MCQ ใช้ `\begin{multicols}{2}` เพื่อประหยัดหน้า

## 5. มาตรฐานคุณภาพ (Quality Standards)

- **ความถูกต้องทางวิชาการ:** ทุกคำตอบและวิธีคำนวณต้องถูกต้อง 100% อ้างอิงจากเนื้อหา PDF
- **ระดับความยาก:** เทียบเท่าข้อสอบปลายภาคจริงของ KMUTT — ไม่ง่ายเกินไป (ต้องคิด) แต่ทำได้ภายใน 3 ชั่วโมง
- **ภาษา:** ภาษาไทยเป็นหลัก ศัพท์เทคนิคใช้ภาษาอังกฤษคู่ขนาน เช่น "Decision Tree (ต้นไม้ตัดสินใจ)"
- **ตัวเลขในโจทย์คำนวณ:** เลือกตัวเลขที่คำนวณแล้วลงตัว (โดยเฉพาะ Entropy ที่ต้องลงตัวจาก log₂) หรือกำหนดค่า log มาให้
- **เฉลยต้องแสดงวิธีทำครบทุกขั้น** ไม่ใช่แค่ตอบสุดท้าย
- **ห้ามคัดลอกโจทย์ตรง ๆ จาก `final_dtmodel.pdf`** — ให้ใช้เป็น pattern อ้างอิงเท่านั้น แล้วสร้างโจทย์ใหม่ที่มีโครงสร้างคล้ายกัน
- **เว้นที่ตอบ** ให้เพียงพอ ไม่ให้นักศึกษาต้องเขียนเบียดกัน
- **ครอบคลุมหัวข้อบังคับจากรุ่นพี่ 3 ครบทั้ง 6 หัวข้อ:**
  1. 4 Model — Part 4.1
  2. Entropy & Information Gain — Part 5.1
  3. Types of Cross-Validation — Part 4.2
  4. Confusion Matrix — Part 5.2
  5. Regression Calculation — Part 5.3
  6. Hierarchical Agglomerative + Dendrogram — Part 5.5

## 6. Output ที่ต้องการ

สร้างไฟล์ **เดียว** ชื่อ `CPE232_Final_MockExam.tex` ที่:

- compile ด้วย XeLaTeX ได้โดยไม่มี error
- มีความยาวประมาณ 30–40 หน้าเมื่อ render เป็น PDF (รวมเฉลย + Formula Sheet + RECAP)
- บันทึกไว้ที่ `c:\Users\CPE KMUTT\Documents\GitHub\cpe232-datamodel-2025\quiz\mock-exam\CPE232_Final_MockExam.tex`

หลังสร้างไฟล์เสร็จ ให้สรุปสั้น ๆ ว่า:

- จำนวนข้อในแต่ละ Part
- การกระจายคะแนนรวม 100 คะแนน (เน้นย้ำว่าเป็นเขียน 90%)
- หัวข้อ Lecture ที่ครอบคลุมในแต่ละข้อ
- หัวข้อบังคับ 6 หัวข้อจากรุ่นพี่ 3 อยู่ในข้อไหนบ้าง
- คำสั่ง compile (เช่น `xelatex CPE232_Final_MockExam.tex`)

===== END PROMPT =====

---

## หมายเหตุการใช้งาน

1. **แนบไฟล์ครบ 6 ไฟล์** ก่อนส่ง Prompt: PDF lecture 4 ไฟล์ + mock exam 2 ไฟล์
2. ถ้า AI ที่ใช้ไม่รองรับ attach PDF โดยตรง ให้ extract เนื้อหา PDF เป็น text/markdown ก่อนแล้วแปะใน context
3. ถ้าต้องการแยกสร้างทีละส่วน (เช่นทำ Part 1 ก่อน แล้วค่อย Part 2) ให้ระบุใน Prompt ว่า "เริ่มจาก Part X เท่านั้น"
4. หลัง compile แล้ว ตรวจสอบโจทย์ Entropy ให้แน่ใจว่าค่า log ลงตัวจริง — ถ้าไม่ลงตัว ให้แก้ตัวเลขใน dataset หรือเพิ่มค่าคงที่ log ในส่วนหัวโจทย์
5. **คำเตือนสำคัญ:** ห้ามให้ AI สร้าง MCQ เกิน 10 คะแนน — เพราะข้อสอบจริงเขียน 90% (รุ่นพี่ 3 ยืนยัน)
