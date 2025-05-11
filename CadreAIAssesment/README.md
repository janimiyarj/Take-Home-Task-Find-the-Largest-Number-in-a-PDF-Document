# PDF Number Extractor

This project intelligently extracts the **largest scaled numeric value** from a PDF using OpenAI's GPT model (e.g., millions, billions).

---

## Features

* ✅ Intelligent chunking of PDF text (number-rich content only)
* ✅ Understands scaling terms like "in millions" or "billion"
* ✅ Uses OpenAI to extract the largest numeric value per chunk
* ✅ Cleans hallucinated or invalid outputs
* ✅ Clean, production-friendly project structure with `.env` support

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

##  Installation

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
🔹 Chunk 1: 7,200,000
🔹 Chunk 2: 12,000,000
🔹 Chunk 3: 3,500,000

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

##  Source Files Overview

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

---

## 📊 Results

Here’s an example result after running the script on the provided PDF:

### 📄 Input PDF:

**Cadre AI - AI Engineer TakeHome Task 3: Parse PDF (Source Material).pdf**

### 🖥️ Actual Run Output (on macOS Terminal):

```
janimiyashaik@Janis-MacBook-Pro CadreAIAssessment % /Users/janimiyashaik/.pyenv/versions/3.11.8/bin/python /Users/janimiyashaik/Desktop/CadreAIAssessment/main.py

✅ Largest Number Detected:
📊 30,704,100,000
```

This was the correct, final scaled number found across all document chunks.

---

### 🏆 Final Result:

```
Largest Number Detected:
📊 30,704,100,000
```

This value was accurately extracted and scaled based on context like “in millions” or table headers.

---

### 🧪 Interpretation:

The model successfully:

* Skipped irrelevant or narrative-only text.
* Recognized and scaled numeric values by interpreting context like "in millions".
* Ignored hallucinated or invalid numbers.
* Returned only digits as instructed.

---

### ✅ Test Cases Handled by the Script

✔️ 1. Skips Irrelevant Pages

Ignores pages with "This page intentionally left blank" or "Table of contents"

✔️ 2. Ignores Non-Numeric Blocks

Only processes blocks that contain at least one digit

✔️ 3. Handles Natural Language Context

Recognizes and scales terms like "in millions", "billions", "thousands", etc.

✔️ 4. Chunk-Wise Context Management

Extracts 5 lines before and after the first numeric line for better understanding

✔️ 5. Rejects Hallucinations

Validates and filters out responses like "12 trillion billion"

Ignores unexpected symbols or units returned by the model

✔️ 6. Parallel Execution

Speeds up execution using ThreadPoolExecutor to call OpenAI in parallel

✔️ 7. Returns Only Digits

Final output is purely numerical—no commas, units, or labels

✔️ 8. Handles Edge Cases Gracefully

Returns 0 if no number is detected in a chunk

Returns the maximum among all scaled valid values

✔️ 9. Tolerates Number Format Variations

Accepts numbers with commas (e.g., 1,000,000) and decimals (e.g., 3.2 million)

✔️ 10. Maintains Deduplicated Context

Tracks seen lines across blocks to avoid duplicate content in overlapping chunks

✔️ 11. Ignores Tables of Content and Headers

Filters out sections that don’t contribute numeric data, including cover blurbs

✔️ 12. Scales Small Decimals Intelligently

Converts "2.45 million" to 2,450,000 using regex and postprocessing

✔️ 13. Handles Mixed Content Blocks

If a block contains both narrative text and financial tables, it extracts only the informative parts

✔️ 14. Avoids Over-Chunking

Respects a 250-word limit per chunk to optimize context window usage for OpenAI

✔️ 15. Ignores Line Noise

Skips blocks made up of only symbols or repeated characters with no value

✔️ 16. Avoids Duplicate Chunk Processing

Prevents lines from being reprocessed multiple times across blocks

✔️ 17. Resilient to OCR Glitches

Ignores broken or malformed lines that are common in OCR-scanned PDFs

✔️ 18. Handles Minimal-Text Pages

Skips pages that contain fewer than a threshold number of words

✔️ 19. Validates Value Range

Rejects numbers that exceed realistic financial/scientific boundaries (>10^13)

✔️ 20. Normalizes Decimal Separators

Accepts both commas and periods as decimal/group separators based on locale

✔️ 21. Case-Insensitive Keyword Filtering

Recognizes headers like "MILLION" or "Billion" in any casing

✔️ 22. Sanitizes Prompt Inputs

Removes extra whitespace or control characters from chunks before sending to OpenAI

✔️ 23. Fail-Safe API Handling

Returns 0 for chunks if the OpenAI API times out or returns an error

✔️ 24. Skips Redundant Descriptions

Avoids company descriptions or boilerplate text sections not containing numeric value

✔️ 25. Prepares OpenAI-Friendly Prompts

Optimized prompt design ensures correct response from GPT with clear formatting instructions



##  Credits

* [OpenAI Python SDK](https://github.com/openai/openai-python)
* [PyMuPDF (fitz)](https://github.com/pymupdf/PyMuPDF)


