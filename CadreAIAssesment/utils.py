import re

# Function to extract and scale the first numeric value from a response string
def extract_first_numeric_value(response_text):
    # Use regex to find a number optionally followed by a scale keyword (e.g., million, billion)
    match = re.search(r"(\d[\d,\.]*)(\s*(million|billion|thousand|trillion))?", response_text.lower())
    
    if match:
        # Remove commas from the matched number string (e.g., "1,000" -> "1000")
        num = match.group(1).replace(",", "")
        # Extract the scale (e.g., million, billion) if present
        scale = match.group(3)
        
        try:
            # Convert the number to a float
            value = float(num)
            
            # Scale the number appropriately
            if scale == "thousand":
                value *= 1_000
            elif scale == "million":
                value *= 1_000_000
            elif scale == "billion":
                value *= 1_000_000_000
            elif scale == "trillion":
                value *= 1_000_000_000_000
            
            return value  # Return the scaled numeric value
        except:
            return 0  # If conversion fails, return 0 as fallback

    return 0  # If no number is found, return 0
