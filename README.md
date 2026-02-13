# � CattoEPUB 📘 — PDF to EPUB Converter & 🐱 CattoTranslate 🌐 — AI Book Translator

แปลง PDF เป็น EPUB ด้วย Typhoon OCR / Gemini Flash + แปลหนังสือ AI (EN↔TH) — ทำงานในเบราว์เซอร์ ไม่ต้องติดตั้ง

🔗 **เข้าใช้ได้ที่:** [https://rainflowdata.github.io/PDF-EPUB-Converter-Thai](https://rainflowdata.github.io/PDF-EPUB-Converter-Thai/)

![Client-Side](https://img.shields.io/badge/Client--Side-JavaScript-yellow)
![Thai OCR](https://img.shields.io/badge/Thai%20OCR-Typhoon-blue)
![Gemini](https://img.shields.io/badge/Gemini-Flash-orange)
![PWA](https://img.shields.io/badge/PWA-Offline-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📱 2 หน้าหลัก

| หน้า | ไฟล์ | คำอธิบาย |
|------|------|----------|
| **� CattoEPUB** | `index.html` | แปลง PDF → EPUB ด้วย OCR (Typhoon/Gemini) |
| **🐱 CattoTranslate** | `translate.html` | แปลหนังสือ PDF/EPUB (EN↔TH) ด้วย AI |

---

## 💡 ที่มาของโปรเจกต์

### Original: Bepub by Ken Takahashi
โปรเจกต์นี้เริ่มต้นจากไอเดียของ **Ken Takahashi** ที่แชร์ใน [ชุมชนนักอ่าน eBook](https://www.facebook.com/groups/ebookreader/posts/25556985560668239) — เป็น Python notebook (Google Colab) ที่ใช้ Typhoon OCR แปลง PDF ภาษาไทยเป็น EPUB ได้

- 🔗 [Colab ต้นฉบับ](https://colab.research.google.com/drive/1lgmYkuEeSUlVDLpplXCnFIQdJP9YMWjw?usp=sharing)
- ใช้ `typhoon-ocr` library + Gradio UI
- ทำงานบน Google Colab (ต้องรัน Python)

### Web Version: by rainflowData
**rainflowData** นำไอเดียมาสร้างเป็น **เว็บแอป** ที่ทำงานได้ในเบราว์เซอร์โดยตรง ไม่ต้องติดตั้งอะไร และเพิ่มฟีเจอร์ใหม่ๆ มากมาย รวมถึงหน้าแปลหนังสือด้วย AI ในชื่อ **CattoEPUB** + **CattoTranslate**

---

## ✨ ฟีเจอร์ทั้งหมด

### 🌐 สถาปัตยกรรม — Client-Side Web App
- ทำงานในเบราว์เซอร์ 100% (PDF.js + JSZip + AI API)
- **PWA** — ติดตั้งเป็น app บนมือถือ/เดสก์ท็อปได้, ทำงาน offline
- **Mobile Ready** — responsive ใช้งานบนมือถือได้
- 🔒 ข้อมูลไม่ผ่านเซิร์ฟเวอร์ (ส่งเฉพาะไปยัง AI API)

### 📘 CattoEPUB — OCR Converter (index.html)

#### 💎 Token Saver Mode (ประหยัด ~85%)
โหมดประหยัด token สำหรับไฟล์ขนาดใหญ่:

**การทำงาน 3 ขั้นตอนต่อหน้า:**
1. **ดึง text จาก PDF** → ถ้าได้ ≥30 ตัวอักษรจริง → ✅ ใช้เลย ฟรี!
2. **ตรวจหน้าว่าง** → ถ้ามีแค่เลขหน้า/ช่องว่าง → ⏭️ ข้าม ไม่เสีย token
3. **ส่ง OCR** → เฉพาะหน้าสแกน/หน้าที่ text น้อย → 🔍 OCR (optimized)

| | ปกติ | Token Saver |
|---|---|---|
| ขนาดภาพ | 1600px PNG | 800px JPEG 50% |
| Max tokens | 16,384 | 4,096 |

#### ⚡ Parallel Processing
- **Token Saver ON** → 5 หน้าพร้อมกัน
- **Token Saver OFF** → 3 หน้าพร้อมกัน

#### 🤖 Multi-Provider OCR

| | 🇹🇭 Typhoon OCR | ✨ Gemini Flash |
|---|---|---|
| ภาษาไทย | ⭐ เก่งมาก | ดี แต่อาจพลาดบ้าง |
| ราคา | ตาม token | **ฟรี!** 15 RPM |
| Model | `typhoon-ocr` | `gemini-2.0-flash` |

#### 🖼️ Smart Image Embed
- ฝังภาพประกอบจริงใน EPUB (เฉพาะ PDF ดิจิทัลที่มีรูปจริง)
- **ไม่ฝังหน้าสแกน** — ป้องกัน EPUB เป็นรูปแปะกระดาษ

#### ✏️ Edit OCR Results
- แก้ไขข้อความ OCR ทีละหน้าก่อนสร้าง EPUB
- มีปุ่ม ◀ ▶ เลื่อนหน้า, บันทึกกลับ localStorage

#### 🛡️ Error Handling & Retry
- **Exponential Backoff** — 429 retry อัตโนมัติ 3 ครั้ง
- **Fatal Error Detection** — 401/402/403 หยุดทันที
- **Auto-stop** — error ติดกัน 3 ครั้ง → หยุดอัตโนมัติ

#### ▶️ Resume & Recovery
- กดหยุด → ปุ่ม **"▶ ต่อจากหน้า X"** โผล่มา
- 💾 localStorage บันทึกอัตโนมัติ — ปิดเว็บกลับมาทำต่อได้
- 📕 อัปโหลด EPUB เดิมเพื่อ resume ได้
- 📥 กู้คืนจาก localStorage → สร้าง EPUB ได้โดยไม่ต้องมี PDF

#### 📊 Stats & Tracking
- สถิติ: หน้าทั้งหมด / Text ฟรี / OCR / ข้าม / Tokens
- 📈 Usage stats รวมทุกครั้ง (sessions, pages, tokens)
- 💰 Cost estimate ก่อนเริ่ม

### 🌐 CattoTranslate — AI Translate (translate.html)

#### 📖 แปลหนังสือด้วย AI
- รองรับ **PDF + EPUB** เป็น input
- แปล **EN↔TH** สลับทิศทางได้
- 4 สไตล์: ธรรมชาติ / เป็นทางการ / สร้างสรรค์ / ตรงตัว
- Context overlap — แปลต่อเนื่องข้ามหน้า

#### 🤖 AI Providers
| | 🇹🇭 Typhoon V2 | ✨ Gemini Flash |
|---|---|---|
| Model | `typhoon-v2.5-30b-a3b-instruct` | `gemini-2.0-flash` |
| ภาษาไทย | ⭐ เก่งมาก | ดี |
| ราคา | ตาม token | ฟรี 15 RPM |

#### 📖 Glossary (คลังศัพท์)
- เพิ่ม/ลบคู่คำศัพท์ (เช่น "Hogwarts → ฮอกวอตส์")
- บันทึกใน localStorage, inject เข้า prompt ทุกหน้าอัตโนมัติ

#### 📖 EPUB Reader
- อ่านผลแปลในเบราว์เซอร์เลยไม่ต้องดาวน์โหลด
- Page navigation ◀ ▶

#### ✏️ Edit Translated Text
- คลิกข้อความแปลในช่อง "เปรียบเทียบ" → แก้ไขได้ทันที
- บันทึกกลับ → สร้าง EPUB ใหม่ได้

#### 💾 Resume & Recovery
- บันทึกอัตโนมัติหลังแปลทุกหน้า
- กู้คืน / แปลต่อ / Export-Import JSON backup
- สารบัญตรวจจับอัตโนมัติ + แก้ไขได้

### 🎨 ฟีเจอร์ร่วม (ทั้ง 2 หน้า)
- 🌙 **Dark Mode** — สลับ Light/Dark ได้
- 🌐 **i18n** — ภาษาไทย / English (OCR page)
- 🔑 **Remember API Key** — จำ key ใน localStorage
- 📄 **PDF Preview** — แสดง thumbnail หน้าแรก
- 🔔 **Browser Notification** — แจ้งเตือนเมื่อเสร็จ
- 🔊 **Sound Notification** — เสียง ding เมื่อเสร็จ
- ⌨️ **Keyboard Shortcuts** — `Ctrl+Enter` = เริ่ม, `Escape` = หยุด/ปิด
- 📈 **Usage Stats** — สถิติรวมทุกครั้ง
- 📑 **สารบัญอัตโนมัติ** — ตรวจจับบท + แก้ไข/เพิ่ม/ลบ + rebuild EPUB

---

## 🚀 วิธีใช้งาน

### ออนไลน์ (GitHub Pages)
เข้าเว็บ → ใช้งานได้เลย!

### Offline
1. ดาวน์โหลดทั้งโปรเจกต์
2. เปิด `index.html` หรือ `translate.html` ในเบราว์เซอร์
3. ใช้งานได้ทันที (ต้องมีเน็ตสำหรับ API เท่านั้น)

### ขั้นตอน CattoEPUB
1. **สมัคร API Key** — [Typhoon](https://opentyphoon.ai) หรือ [Gemini](https://aistudio.google.com/apikey) (ฟรี)
2. **อัปโหลด PDF** → เปิด Token Saver (แนะนำ)
3. **กด "เริ่มแปลงไฟล์"** → ดาวน์โหลด EPUB + TXT

### ขั้นตอน CattoTranslate
1. **อัปโหลด PDF/EPUB** → เลือกทิศทาง EN↔TH
2. **เลือกสไตล์** + เพิ่ม Glossary (ถ้าต้องการ)
3. **กด "เริ่มแปล"** → อ่าน/แก้ไข/ดาวน์โหลด EPUB

---

## 🛠️ เทคโนโลยี

| ส่วน | เทคโนโลยี |
|------|-----------|
| PDF อ่าน | [PDF.js](https://mozilla.github.io/pdf.js/) 3.11.174 |
| EPUB สร้าง | [JSZip](https://stuk.github.io/jszip/) 3.10.1 |
| OCR | [Typhoon OCR](https://opentyphoon.ai) `typhoon-ocr` |
| Translation | [Typhoon V2](https://opentyphoon.ai) `typhoon-v2.5-30b-a3b-instruct` |
| AI (ฟรี) | [Gemini Flash](https://aistudio.google.com/apikey) `gemini-2.0-flash` |
| UI | Vanilla HTML/CSS/JS |
| Font | Sarabun, Plus Jakarta Sans, JetBrains Mono |
| PWA | Service Worker + manifest.json |

---

## 📁 โครงสร้างไฟล์

```
epub_convert/
├── index.html        ← 🐱 CattoEPUB — OCR Converter
├── translate.html    ← 🐱 CattoTranslate — AI Book Translator
├── manifest.json     ← PWA manifest
├── sw.js             ← Service Worker (offline caching)
├── rainflow.png      ← Logo
├── fix_epub.py       ← 🔧 Script ซ่อม EPUB ที่มีรูปฝังเกิน
├── check_epub.py     ← 🔍 Script ตรวจสอบเนื้อหา EPUB
└── README.md         ← ไฟล์นี้
```

---

## ⚖️ เปรียบเทียบ Colab vs Web

| | Colab (ต้นฉบับ) | Web (เวอร์ชันนี้) |
|---|---|---|
| สภาพแวดล้อม | Google Colab (Python) | เบราว์เซอร์ |
| ติดตั้ง | ต้อง pip install | ไม่ต้อง (PWA) |
| Token Saver | ❌ | ✅ ประหยัด ~85% |
| Parallel | ❌ ทีละหน้า | ✅ 3-5 หน้าพร้อมกัน |
| Resume | ❌ | ✅ ปิดเว็บกลับมาต่อได้ |
| Error Handling | พื้นฐาน | ✅ Retry + Auto-stop |
| สารบัญ | ❌ | ✅ ตรวจจับ + แก้ไขได้ |
| Cover | ❌ | ✅ ใส่ปกได้ |
| แปลหนังสือ | ❌ | ✅ CattoTranslate EN↔TH |
| Glossary | ❌ | ✅ คลังศัพท์ |
| EPUB Reader | ❌ | ✅ อ่านในเบราว์เซอร์ |
| Edit Text | ❌ | ✅ แก้ไขก่อนสร้าง EPUB |
| Dark Mode | ❌ | ✅ |
| Mobile | ❌ | ✅ Responsive + PWA |
| Multi-Provider | ❌ Typhoon อย่างเดียว | ✅ Typhoon + Gemini Flash |

---

## 🙏 Credits

- **Ken Takahashi** — ไอเดียและ Colab ต้นฉบับ ([Facebook](https://www.facebook.com/groups/ebookreader/posts/25556985560668239) · [Colab](https://colab.research.google.com/drive/1lgmYkuEeSUlVDLpplXCnFIQdJP9YMWjw?usp=sharing))
- **rainflowData** — Web adaptation + ฟีเจอร์เพิ่มเติมทั้งหมด
- **Typhoon** by [SCB 10X](https://opentyphoon.ai) — Thai OCR & Translation API
- **Gemini Flash** by [Google](https://aistudio.google.com/apikey) — Free AI API
- แชร์ใน [ชุมชนนักอ่าน eBook](https://www.facebook.com/groups/778412228952249/)

---

## 📄 License

MIT License — ใช้ได้อิสระ ดัดแปลงได้ ขอแค่ให้เครดิต
