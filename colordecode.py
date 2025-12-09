from PIL import Image
import base64
import binascii
from main import CHARACTER_COLOR_MAP


def _build_inverse_map(char_map):
    """Return a dict mapping hex color (upper) to character."""
    inv = {}
    for k, v in char_map.items():
        inv[v.upper()] = k
    return inv


def decode_image_to_chars(image_path="encoded_image.png"):
    """Decode an image created by colorencode into a sequence of characters.

    Returns the decoded string (characters mapped from pixel colors). Unknown
    colors are replaced with '?'.
    """
    inv_map = _build_inverse_map(CHARACTER_COLOR_MAP)

    # Keep alpha channel so we can detect transparent pixels
    img = Image.open(image_path).convert('RGBA')
    w, h = img.size

    chars = []
    for y in range(h):
        for x in range(w):
            r, g, b, a = img.getpixel((x, y))
            # If pixel is fully transparent, treat as unused and skip
            if a == 0:
                continue

            hex_color = '#{0:02X}{1:02X}{2:02X}'.format(r, g, b)
            ch = inv_map.get(hex_color)
            if ch is None:
                # Unknown color: mark with '?'
                chars.append('?')
            else:
                chars.append(ch)

    return ''.join(chars)


def try_base64_decode(s):
    """Try to base64-decode the string `s`. Return decoded text if successful, else None."""
    try:
        # base64 should be ascii-safe
        decoded = base64.b64decode(s, validate=True)
        try:
            return decoded.decode('utf-8')
        except UnicodeDecodeError:
            # Return bytes repr if not valid UTF-8
            return decoded
    except (binascii.Error, ValueError):
        return None


def main():
    img_path = "encoded_image.png"
    print(f"Decoding image: {img_path}")
    decoded_chars = decode_image_to_chars(img_path)
    # Print the raw decoded characters (before attempting base64 decode)
    print("\nDecoded characters from image:")
    print(decoded_chars)

    # Save the raw decoded characters (likely a base64 string) to file
    with open('decoded_base64.txt', 'w', encoding='utf-8') as f:
        f.write(decoded_chars)
    print("Saved decoded characters to decoded_base64.txt")

    # Try to interpret as base64 and decode
    decoded_text = try_base64_decode(decoded_chars)
    if decoded_text is not None:
        out_path = 'decoded_text.txt'
        mode = 'wb' if isinstance(decoded_text, (bytes, bytearray)) else 'w'
        with open(out_path, mode) as f:
            if isinstance(decoded_text, (bytes, bytearray)):
                f.write(decoded_text)
            else:
                f.write(decoded_text)
        print(f"Base64 decode successful — saved to {out_path}")
    else:
        print("Decoded characters do not appear to be valid base64 or decoding failed.")


if __name__ == '__main__':
    main()
