# Import the function to extract text chunks from the PDF
from extractor import extract_text_chunks

# Import the function to query OpenAI for the largest number in a chunk
from openai_agent import ask_openai_for_max

# Import API key loader from the config file
from config import get_api_key

# Import thread pool executor for parallel processing
from concurrent.futures import ThreadPoolExecutor

# Main function to find the largest number in a PDF
def find_largest_number(pdf_path):
    # Step 1: Extract meaningful, number-rich chunks from the PDF
    chunks = extract_text_chunks(pdf_path)

    # Step 2: Load OpenAI API key from environment or .env file
    api_key = get_api_key()

    # Step 3: Store numeric values returned by the OpenAI model
    max_values = []

    # Step 4: Function to process a chunk and get the largest number from it
    def process_chunk(idx_chunk):
        idx, chunk = idx_chunk
        val = ask_openai_for_max(chunk, api_key)  # Call OpenAI for this chunk
        return val

    # Step 5: Use ThreadPoolExecutor to parallelize OpenAI calls
    with ThreadPoolExecutor() as executor:
        max_values = list(executor.map(process_chunk, enumerate(chunks)))

    # Step 6: Compute the overall largest value from all chunks
    max_val = max(max_values)

    # Step 7: Output the result in readable format
    print("\n Largest Number Detected:")
    print(f"{int(max_val):,}")

# Entry point of the script
if __name__ == "__main__":
    # Specify the PDF to scan
    find_largest_number("Cadre AI - AI Engineer TakeHome Task 3_ Parse PDF (Source Material).pdf")
