import fitz  # PyMuPDF

def extract_text_chunks(pdf_path, max_chunk_words=250):
    doc = fitz.open(pdf_path)
    chunks = []
    current_chunk = []
    seen_lines = set()
    word_count = 0

    for page in doc:
        blocks = page.get_text("blocks")
        blocks.sort(key=lambda b: (round(b[1]), round(b[0])))

        for block in blocks:
            text = block[4].strip()
            if not text:
                continue
            if text.lower() in ["this page intentionally left blank", "table of contents"]:
                continue
            if not any(char.isdigit() for char in text):
                continue

            lines = text.split("\n") if "\n" in text else [text]
            block_snippet = []
            for idx, line in enumerate(lines):
                if any(char.isdigit() for char in line):
                    context_lines = lines[max(0, idx - 5): idx + 6]
                    for ctx_line in context_lines:
                        if ctx_line not in seen_lines:
                            seen_lines.add(ctx_line)
                            block_snippet.append(ctx_line)
                    break

            if block_snippet:
                for line in block_snippet:
                    current_chunk.append(line.strip())
                    word_count += len(line.split())
                    if word_count >= max_chunk_words:
                        chunks.append("\n".join(current_chunk))
                        current_chunk = []
                        word_count = 0

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks
