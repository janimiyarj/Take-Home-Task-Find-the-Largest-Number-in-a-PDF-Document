from openai import OpenAI
from utils import extract_first_numeric_value

def ask_openai_for_max(text_chunk, api_key):
    client = OpenAI(api_key=api_key)
    prompt = f"""
You are a highly specialized AI assistant built to extract financial intelligence from government documents.

Task:
Find the single largest numeric value from the following document segment. Consider:

1. 📄 **Paragraphs** — Scale numbers using nearby terms like "in millions" or "in billions". Skip narrative-only text.
2. 📊 **Tables** — Understand headers, subheaders, rows, columns, and notes. Scale all values if the table mentions a unit.
3. 📈 **Graphs** — Treat axis labels and data points as contextual indicators. Extract the highest value displayed.
4. 📌 **Images/Diagrams** — Consider visible text, numerical references, or calculated figures if legible.
5. ⛔ **Ignore** footers, TOCs, cover pages, or descriptive blurbs with no numbers.

Output:
Only return the single largest **scaled** number. Use digits only, no units, no commas, no explanation.
Examples: 23000000, 925000000, 30704100000

---
{text_chunk}

Answer:
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20,
            temperature=0
        )
        result = response.choices[0].message.content.strip()
        val = extract_first_numeric_value(result)
        if val > 0 and val <= 10**13:
            return val
        print(f"⚠️ Rejected hallucinated/invalid value: {result}")
        return 0
    except Exception as e:
        print(f"❌ OpenAI Error: {e}")
        return 0
