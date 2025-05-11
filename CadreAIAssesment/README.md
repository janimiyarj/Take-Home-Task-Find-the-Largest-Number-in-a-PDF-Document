# 📊 PDF Number Extractor

This project intelligently extracts the **largest scaled numeric value** from a PDF using OpenAI's GPT model (e.g., millions, billions).

---

## 🚀 Features

* ✅ Intelligent chunking of PDF text (number-rich content only)
* ✅ Understands scaling terms like "in millions" or "billion"
* ✅ Uses OpenAI to extract the largest numeric value per chunk
* ✅ Cleans hallucinated or invalid outputs
* ✅ Clean, production-friendly project structure with `.env` support

---

## 📁 Project Structure

```
pdf_number_extractor/
├── main.py               # Main entry point
├── extractor.py          # PDF chunking logic using PyMuPDF
├── openai_agent.py       # Prompt OpenAI and validate response
├── utils.py              # Numeric value extractor & scaler
├── config.py             # Loads OpenAI API key from .env
├── requirements.txt      # Python dependencies
├── .env                  # API key (excluded from version control)
└── README.md             # This file
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf_number_extractor.git
cd pdf_number_extractor
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add your OpenAI API key

Create a `.env` file in the root folder:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> 🔒 **Important:** Keep your `.env` file private and add it to `.gitignore`.

---

## ▶️ Running the Script

1. Place your target PDF file in the root folder.
2. Open `main.py` and make sure the correct filename is provided.
3. Run the script:

```bash
python main.py
```

Example output:

```
🔹 Chunk 1: 7,200,000
🔹 Chunk 2: 12,000,000
🔹 Chunk 3: 3,500,000

✅ Largest Number Detected:
📊 12,000,000
```

---

## 🔐 .gitignore

Create a `.gitignore` file in the root with the following content:

```
.env
__pycache__/
*.pyc
*.pyo
*.DS_Store
venv/
```

---

## 📦 Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt
```

### Dependencies:

```
openai>=1.0.0
PyMuPDF>=1.23.7
python-dotenv
```

---

## 📄 Source Files Overview

### `main.py`

Runs the end-to-end pipeline: extracts chunks, sends them to OpenAI, and prints the largest number.

### `extractor.py`

Extracts context-rich chunks from PDF using PyMuPDF. Skips irrelevant text and captures digit-heavy content.

### `openai_agent.py`

Contains the prompt template and logic to send each chunk to OpenAI and validate the numeric response.

### `utils.py`

Parses and scales numbers like "23 million" into `23000000`. Supports thousands, millions, billions, trillions.

### `config.py`

Loads OpenAI API key securely from the `.env` file using `python-dotenv`.

---

## 🧠 Credits

* [OpenAI Python SDK](https://github.com/openai/openai-python)
* [PyMuPDF (fitz)](https://github.com/pymupdf/PyMuPDF)

---

## 🙋‍♂️ Support

Need help customizing or deploying this as an API? Open an issue or reach out directly
