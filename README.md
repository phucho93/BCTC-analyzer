# 📊 BCTC Analyzer Pro — CFA Framework

> Upload PDF BCTC → Claude phân tích → Paste JSON → Dashboard tự động render

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

---

## 🔄 Workflow

```
PDF scan BCTC (3 năm)
        ↓
   Claude extract + phân tích
   (dùng PROMPT_CHUAN.txt)
        ↓
   JSON chuẩn hóa
        ↓
   Paste vào app
        ↓
   Dashboard tự động render
```

---

## 📋 Sử dụng

### Bước 1: Chuẩn bị prompt

Mở file `PROMPT_CHUAN.txt`, copy toàn bộ nội dung.

### Bước 2: Phân tích với Claude

1. Mở [claude.ai](https://claude.ai) → New chat
2. Paste prompt vào
3. Đính kèm file PDF BCTC (3 năm, có thể là bản scan)
4. Gửi → chờ Claude trả về JSON

### Bước 3: Render dashboard

1. Mở app Streamlit
2. Copy JSON từ Claude
3. Paste vào sidebar → Click **"Phân tích"**
4. Dashboard render tự động

---

## 🖥️ Chạy local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Deploy Streamlit Cloud

1. Push repo lên GitHub
2. Vào [share.streamlit.io](https://share.streamlit.io) → New app
3. Chọn repo, branch `main`, file `app.py`
4. Deploy

---

## 📁 Cấu trúc

```
bctc-analyzer/
├── app.py                  ← Dashboard chính (6 tabs)
├── PROMPT_CHUAN.txt        ← Prompt dùng với Claude
├── requirements.txt
├── .streamlit/config.toml
└── utils/
    └── sample_data.py      ← Dữ liệu demo
```

---

## 📊 Dashboard gồm 6 tabs

| Tab | Nội dung |
|-----|----------|
| 📈 Tổng quan & BCTC | IS / BS / CF tables + trend charts |
| 🔬 Chỉ số CFA | Profitability / Leverage / Efficiency / DuPont |
| 🏆 Chất lượng & Flags | Quality Score radar + Investment Thesis + Red/Green Flags |
| 🔮 Định giá & DCF | Bull/Base/Bear + Multiples + Valuation range chart |
| 📊 Dự phóng | 5-year projection chart + assumptions |
| ⚖️ Altman & Beneish | Z-Score gauge + M-Score table |

---

## ⚠️ Disclaimer

Công cụ phục vụ nghiên cứu và học tập. Không phải lời khuyên đầu tư.
