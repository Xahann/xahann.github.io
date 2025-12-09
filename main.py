# Alphabet to color mapping (shades of red, similar hues)
ALPHABET_COLOR_MAP = {
    'a': '#A01414', 'b': '#A11414', 'c': '#A21414', 'd': '#A31414',
    'e': '#A41414', 'f': '#A51414', 'g': '#A61414', 'h': '#A71414',
    'i': '#A81414', 'j': '#A91414', 'k': '#AA1414', 'l': '#AB1414',
    'm': '#AC1414', 'n': '#AD1414', 'o': '#AE1414', 'p': '#AF1414',
    'q': '#B01414', 'r': '#B11414', 's': '#B21414', 't': '#B31414',
    'u': '#B41414', 'v': '#B51414', 'w': '#B61414', 'x': '#B71414',
    'y': '#B81414', 'z': '#B91414'
}

# Numbers to color mapping (continuing shades of red)
NUMBERS_COLOR_MAP = {
    '0': '#BA1414', '1': '#BB1414', '2': '#BC1414', '3': '#BD1414',
    '4': '#BE1414', '5': '#BF1414', '6': '#C01414', '7': '#C11414',
    '8': '#C21414', '9': '#C31414'
}

# Special characters to color mapping (continuing shades of red)
SPECIAL_CHAR_COLOR_MAP = {
    ' ': '#C41414',   # Space
    ',': '#C51414',   # Comma
    '.': '#C61414',   # Period
    '/': '#C71414',   # Forward slash
    ')': '#C81414',   # Close paren
    '(': '#C91414',   # Open paren
    ']': '#CA1414',   # Close bracket
    '[': '#CB1414',   # Open bracket
    '^': '#CC1414',   # Caret
    '%': '#CD1414',   # Percent
    '$': '#CE1414',   # Dollar
    '#': '#CF1414',   # Hash
    '@': '#D01414',   # At sign
    '!': '#D11414',   # Exclamation
    '?': '#D21414',   # Question mark
    '+': '#D31414',   # Plus
    '=': '#D41414'    # Equals (padding)
}

# Uppercase letters mapping (A-Z) for base64 support, also shades of red
UPPERCASE_COLOR_MAP = {
    'A': '#D51414', 'B': '#D61414', 'C': '#D71414', 'D': '#D81414',
    'E': '#D91414', 'F': '#DA1414', 'G': '#DB1414', 'H': '#DC1414',
    'I': '#DD1414', 'J': '#DE1414', 'K': '#DF1414', 'L': '#E01414',
    'M': '#E11414', 'N': '#E21414', 'O': '#E31414', 'P': '#E41414',
    'Q': '#E51414', 'R': '#E61414', 'S': '#E71414', 'T': '#E81414',
    'U': '#E91414', 'V': '#EA1414', 'W': '#EB1414', 'X': '#EC1414',
    'Y': '#ED1414', 'Z': '#EE1414'
}

# Combined color map (include uppercase letters)
CHARACTER_COLOR_MAP = {**ALPHABET_COLOR_MAP, **UPPERCASE_COLOR_MAP, **NUMBERS_COLOR_MAP, **SPECIAL_CHAR_COLOR_MAP}


def text_to_color_hex(text):
    """Convert each character in text to a color hex code based on the character mapping."""
    result = {}
    
    for char in text.lower():
        if char in CHARACTER_COLOR_MAP:
            result[char] = CHARACTER_COLOR_MAP[char]
    
    return result


def text_to_color_hex_list(text):
    """Convert text to a list of hex codes (preserving order of all characters)."""
    encodedText = []
    
    for char in text.lower():
        if char in CHARACTER_COLOR_MAP:
            encodedText.append(CHARACTER_COLOR_MAP[char])
    
    return encodedText


def encode_to_base64_and_save(encodedText, filename="hexText.txt"):
    """
    Encode the hex code list to base64 and save it to a text file.
    
    Args:
        encodedText: List of hex color codes
        filename: Output filename
    """
    import base64
    import json
    
    # Convert list to JSON string
    json_str = json.dumps(encodedText)
    
    # Encode to base64
    base64_encoded = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    
    # Save to file as bytes to avoid newline/encoding issues
    with open(filename, 'wb') as f:
        f.write(base64_encoded.encode('utf-8'))

    # Verify by decoding immediately
    import base64 as _b64
    try:
        _b64.b64decode(base64_encoded.encode('utf-8'), validate=True)
        ok_msg = "OK"
    except Exception:
        ok_msg = "FAILED"

    print(f"\nEncoded text saved to {filename} ({ok_msg})")
    print(f"Base64 encoded (first 50 chars): {base64_encoded[:50]}..." if len(base64_encoded) > 50 else f"Base64 encoded: {base64_encoded}")

    return base64_encoded

def encode_raw_text_to_base64_and_save(text, filename="hexText.txt"):
    """
    Encode raw input text to base64 and save it to a text file.

    This saves the raw text (not converted to hex codes) as a base64 string.
    """
    import base64

    if text is None:
        print("No text provided to encode.")
        return None

    raw_bytes = text.encode('utf-8')
    base64_encoded = base64.b64encode(raw_bytes).decode('utf-8')

    # Write base64 as bytes to avoid accidental encoding/line ending issues
    with open(filename, 'wb') as f:
        f.write(base64_encoded.encode('utf-8'))

    # Verify by decoding immediately
    import base64 as _b64
    try:
        _b64.b64decode(base64_encoded.encode('utf-8'), validate=True)
        ok_msg = "OK"
    except Exception:
        ok_msg = "FAILED"

    print(f"\nRaw text base64-encoded and saved to {filename} ({ok_msg})")
    print(f"Base64 (first 60 chars): {base64_encoded[:60]}..." if len(base64_encoded) > 60 else f"Base64: {base64_encoded}")
    return base64_encoded

def main():
    # Display the character to color mapping
    print("Character Color Mapping:")
    print("-" * 40)
    
    print("\nLetters (A-Z):")
    for letter in sorted(ALPHABET_COLOR_MAP.keys()):
        print(f"  {letter}: {ALPHABET_COLOR_MAP[letter]}", end="  ")
        if (list(ALPHABET_COLOR_MAP.keys()).index(letter) + 1) % 3 == 0:
            print()
    
    print("\n\nNumbers (0-9):")
    for num in sorted(NUMBERS_COLOR_MAP.keys()):
        print(f"  {num}: {NUMBERS_COLOR_MAP[num]}", end="  ")
        if (int(num) + 1) % 3 == 0:
            print()
    
    print("\n\nSpecial Characters:")
    for char in sorted(SPECIAL_CHAR_COLOR_MAP.keys()):
        char_display = repr(char) if char == ' ' else char
        print(f"  {char_display}: {SPECIAL_CHAR_COLOR_MAP[char]}", end="  ")
    
    print("\n" + "=" * 40)
    user_input = input("\nEnter text to encode (will be saved base64 to hexText.txt): ")

    # Do NOT convert input to hex codes here; only base64-encode the raw text.
    if user_input:
        encode_raw_text_to_base64_and_save(user_input)
    else:
        print("No input provided; nothing saved.")


if __name__ == "__main__":
    main()