import re

def extract_first_numeric_value(response_text):
    match = re.search(r"(\d[\d,\.]*)(\s*(million|billion|thousand|trillion))?", response_text.lower())
    if match:
        num = match.group(1).replace(",", "")
        scale = match.group(3)
        try:
            value = float(num)
            if scale == "thousand":
                value *= 1_000
            elif scale == "million":
                value *= 1_000_000
            elif scale == "billion":
                value *= 1_000_000_000
            elif scale == "trillion":
                value *= 1_000_000_000_000
            return value
        except:
            return 0
    return 0
