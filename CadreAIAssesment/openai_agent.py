from openai import OpenAI
from utils import extract_first_numeric_value

# Function to ask OpenAI for the largest numeric value in a given text chunk
def ask_openai_for_max(text_chunk, api_key):
    # Initialize the OpenAI client with the provided API key
    client = OpenAI(api_key=api_key)

    # Craft a system prompt that instructs the model how to extract and scale values
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
        # Send the prompt to the GPT model
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use GPT-3.5 Turbo model
            messages=[{"role": "user", "content": prompt}],  # User message format
            max_tokens=20,  # Limit response to short number only
            temperature=0    # Make output deterministic
        )

        # Extract and clean the model's response
        result = response.choices[0].message.content.strip()

        # Use regex helper to extract and scale the numeric value
        val = extract_first_numeric_value(result)

        # Only return values that are realistic and within upper bounds
        if val > 0 and val <= 10**13:
            return val

        # Print a warning if the value is invalid or hallucinated
        print(f"⚠️ Rejected hallucinated/invalid value: {result}")
        return 0

    except Exception as e:
        # Handle any exceptions from OpenAI API call
        print(f"❌ OpenAI Error: {e}")
        return 0
