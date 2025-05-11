import fitz  # PyMuPDF

# Function to extract context-rich, token-efficient text chunks from a PDF
def extract_text_chunks(pdf_path, max_chunk_words=250):
    doc = fitz.open(pdf_path)  # Open the PDF file
    chunks = []                # List to hold all final text chunks
    current_chunk = []         # Temporarily holds lines for the current chunk
    seen_lines = set()         # To avoid processing duplicate lines
    word_count = 0             # Track words per chunk

    for page in doc:
        # Extract text blocks from the page
        blocks = page.get_text("blocks")
        # Sort blocks top-to-bottom, left-to-right (spatial order)
        blocks.sort(key=lambda b: (round(b[1]), round(b[0])))

        for block in blocks:
            text = block[4].strip()  # Get the actual text content from the block
            if not text:
                continue  # Skip empty blocks

            # Skip common irrelevant phrases
            if text.lower() in ["this page intentionally left blank", "table of contents"]:
                continue

            # Skip text blocks without any digits
            if not any(char.isdigit() for char in text):
                continue

            # Split text into lines
            lines = text.split("\n") if "\n" in text else [text]
            block_snippet = []

            # Find the first line with a digit and extract 5 lines before and after
            for idx, line in enumerate(lines):
                if any(char.isdigit() for char in line):
                    context_lines = lines[max(0, idx - 5): idx + 6]  # 5 lines before & after
                    for ctx_line in context_lines:
                        if ctx_line not in seen_lines:
                            seen_lines.add(ctx_line)
                            block_snippet.append(ctx_line)
                    break  # Only one such snippet per block

            # If we got a valid snippet, add its lines to the current chunk
            if block_snippet:
                for line in block_snippet:
                    current_chunk.append(line.strip())
                    word_count += len(line.split())

                    # Once the chunk reaches the word limit, store and reset
                    if word_count >= max_chunk_words:
                        chunks.append("\n".join(current_chunk))
                        current_chunk = []
                        word_count = 0

    # Add any remaining text as the last chunk
    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks  # Return all text chunks for further processing
