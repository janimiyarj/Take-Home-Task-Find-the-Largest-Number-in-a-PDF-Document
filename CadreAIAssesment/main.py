from extractor import extract_text_chunks
from openai_agent import ask_openai_for_max
from config import get_api_key
from concurrent.futures import ThreadPoolExecutor

def find_largest_number(pdf_path):
    chunks = extract_text_chunks(pdf_path)
    api_key = get_api_key()
    max_values = []

    def process_chunk(idx_chunk):
        idx, chunk = idx_chunk
        val = ask_openai_for_max(chunk, api_key)
        return val

    with ThreadPoolExecutor() as executor:
        max_values = list(executor.map(process_chunk, enumerate(chunks)))

    max_val = max(max_values)
    print("\n✅ Largest Number Detected:")
    print(f"📊 {int(max_val):,}")

if __name__ == "__main__":
    find_largest_number("Cadre AI - AI Engineer TakeHome Task 3_ Parse PDF (Source Material).pdf")
