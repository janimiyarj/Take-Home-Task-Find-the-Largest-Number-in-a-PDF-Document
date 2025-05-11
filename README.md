# Take-Home-Task-Find-the-Largest-Number-in-a-PDF-Document

This project intelligently extracts the **largest scaled numeric value** from a PDF using OpenAI's GPT model (e.g., millions, billions).

---

## Features

* Intelligent chunking of PDF text (number-rich content only)
* Understands scaling terms like "in millions" or "billion"
* Uses OpenAI to extract the largest numeric value per chunk
* Cleans hallucinated or invalid outputs
* Clean, production-friendly project structure with `.env` support

---

## Project Structure

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

## Installation

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

>  **Important:** Keep your `.env` file private and add it to `.gitignore`.

---

## Running the Script

1. Place your target PDF file in the root folder.
2. Open `main.py` and make sure the correct filename is provided.
3. Run the script:

```bash
python main.py
```

Example output:

```
Chunk 1: 7,200,000
Chunk 2: 12,000,000
Chunk 3: 3,500,000

Largest Number Detected:
12,000,000
```

---

## .gitignore

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

## Requirements

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

## Source Files Overview

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

## Test Cases Handled

- **Different Numeric Formats Handled**:
  - `23 million`, `3.5 billion`, `4.25k`, `700 thousand` → Automatically scaled using regex and multiplier logic
  - `12,000,000`, `2,450,000.50`, `13.5` → Normalized with locale-aware comma/decimal parsing
  - `€2.5 million`, `USD 3 billion`, `$5.2M` → Extracted and cleaned from currency symbols and suffixes
  - `increased by 12 million`, `loss of 3 billion`, `projected to be 7.2B` → Extracted from natural language context
  - Tables with values like `Total Revenue | 2,340,000` or `Net Loss (in millions): 3.1` → Captured with chunking logic and line filtering

- Skips irrelevant pages (blank or TOC)  
- Extracts only numeric-rich content  
- Scales terms like "million", "billion", "k", "thousand"  
- 5-line context window around numeric entries  
- Rejects invalid/hallucinated responses like "12 trillion billion"  
- Threaded OpenAI API calls for speed  
- Standardizes output as plain digits (no labels or symbols)  
- Handles OCR errors and malformed content  
- Rejects extreme/unrealistic values (>10^13)  
- Deduplicated lines across overlapping chunks  
- Skips narrative-only or boilerplate sections  
- Normalizes comma/decimal use per locale (e.g., 1.000,5 or 1,000.5)  
- Prepares OpenAI-friendly prompts to prevent hallucination  
- Fallbacks to 0 if no number is detected or API fails  
- Filters symbols/line noise and removes redundant corporate blurbs

---

## Model Comparison

| Model      | Speed       | Accuracy         | Notes                                   |
|------------|-------------|------------------|-----------------------------------------|
| **GPT (OpenAI)** | Moderate | High            | Most accurate for numeric parsing       |
| **Claude**       | Super fast | Hallucinates     | Fast but often generates wrong values   |
| **Gemini**       | Inconsistent | Low             | Often fails to identify relevant values |


## Credits

* [OpenAI Python SDK](https://github.com/openai/openai-python)
* [PyMuPDF (fitz)](https://github.com/pymupdf/PyMuPDF)

---

## About Author:

Name of the Author: Jani Miya Shaik

Email: janimiyask72@gmail.com




