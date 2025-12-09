from main import text_to_color_hex_list, CHARACTER_COLOR_MAP
from PIL import Image
import math
import base64
import json


def create_image_from_encoded_text(encodedText, filename="encoded_image.png", square=True):
    """
    Create an image where each hex color in encodedText represents one pixel.
    
    Args:
        encodedText: List of hex color codes
        filename: Output image filename
    """
    if not encodedText:
        print("No encoded text to create image from.")
        return
    
    # Filter out spaces, keep only hex codes
    colors = [color for color in encodedText if color != ' ']
    
    if not colors:
        print("No color data found.")
        return
    
    num_pixels = len(colors)

    if square:
        # Calculate side length for square image
        side_length = math.ceil(math.sqrt(num_pixels))
        width = side_length
        height = side_length
        # Use RGBA so unused pixels can be transparent
        img = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))
        pixels = img.load()

        # Fill pixels row-wise; leave remaining pixels transparent
        pixel_index = 0
        for y in range(height):
            for x in range(width):
                if pixel_index < num_pixels:
                    hex_color = colors[pixel_index]
                    rgb = tuple(int(hex_color.lstrip('#')[j:j+2], 16) for j in (0, 2, 4))
                    pixels[x, y] = (rgb[0], rgb[1], rgb[2], 255)
                    pixel_index += 1
                else:
                    # leave as transparent
                    continue

    else:
        # 1-pixel-high image (same as before) using RGBA
        width = num_pixels
        height = 1
        img = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))
        pixels = img.load()
        for i, hex_color in enumerate(colors):
            rgb = tuple(int(hex_color.lstrip('#')[j:j+2], 16) for j in (0, 2, 4))
            pixels[i, 0] = (rgb[0], rgb[1], rgb[2], 255)

    img.save(filename)
    print(f"Image saved as {filename}")
    print(f"Image size: {width}x{height} pixels ({num_pixels} color pixels)")
    return img


def create_image_from_file(filename="hexText.txt", square=True):
    """
    Create an image directly from hex colors in a file (no decoding).
    
    Args:
        filename: Input filename containing hex colors
    """
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
        
        # Split the content by whitespace or commas to get individual hex codes
        hex_codes = content.replace(',', ' ').split()
        
        # Filter valid hex codes
        valid_colors = [color.strip() for color in hex_codes if color.startswith('#')]
        
        if not valid_colors:
            print(f"No valid hex codes found in {filename}")
            return None
        
        num_pixels = len(valid_colors)

        if square:
            side_length = math.ceil(math.sqrt(num_pixels))
            width = side_length
            height = side_length
            img = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))
            pixels = img.load()

            pixel_index = 0
            for y in range(height):
                for x in range(width):
                    if pixel_index < num_pixels:
                        hex_color = valid_colors[pixel_index]
                        rgb = tuple(int(hex_color.lstrip('#')[j:j+2], 16) for j in (0, 2, 4))
                        pixels[x, y] = (rgb[0], rgb[1], rgb[2], 255)
                        pixel_index += 1
                    else:
                        # leave transparent
                        continue
        else:
            width = num_pixels
            height = 1
            img = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))
            pixels = img.load()
            for i, hex_color in enumerate(valid_colors):
                rgb = tuple(int(hex_color.lstrip('#')[j:j+2], 16) for j in (0, 2, 4))
                pixels[i, 0] = (rgb[0], rgb[1], rgb[2], 255)

        img.save("encoded_image.png")
        print(f"Image created from {filename}")
        print(f"Image size: {width}x{height} pixels ({num_pixels} color pixels)")
        return img
    
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except Exception as e:
        print(f"Error creating image: {e}")
        return None


def convert_file_text_to_hex_codes(filename="hexText.txt"):
    """
    Read text from a file and convert each character to hex codes using CHARACTER_COLOR_MAP.
    
    Args:
        filename: Input filename
    
    Returns:
        List of hex color codes
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        # Convert each character to hex code using the character map
        # Preserve case because base64 is case-sensitive
        encodedText = []
        for char in content:
            if char in CHARACTER_COLOR_MAP:
                encodedText.append(CHARACTER_COLOR_MAP[char])
        
        print(f"Successfully converted text from {filename}")
        print(f"Total characters encoded: {len(encodedText)}")
        return encodedText
    
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except Exception as e:
        print(f"Error converting file: {e}")
        return None


def main():
    # Read text from hexText.txt, convert each character to hex codes, and create image
    encodedText = convert_file_text_to_hex_codes("hexText.txt")
    
    if encodedText:
        print(f"\nEncoded text: {encodedText[:10]}..." if len(encodedText) > 10 else f"\nEncoded text: {encodedText}")
        create_image_from_encoded_text(encodedText)
    else:
        print("Unable to process hexText.txt")


if __name__ == "__main__":
    main()
