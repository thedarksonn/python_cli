## ascii art stands for american standard code for information interchange art

# it is a form of visual art that uses characters from the ASCII character set to create images or designs.
# ASCII art uses combinations of characters like #, *, /, and | to represent shapes, figures, and patterns.

# You can achieve this by using simple string manipulation or by leveraging libraries designed for creating and displaying ASCII art. 
# Here's how you can do both



## using plain text
# def print_ascii_art():
#     art = r"""
#       ____  
#      / ___| __ _ _ __ ___   ___ 
#     | |  _ / _` | '_ ` _ \ / _ \
#     | |_| | (_| | | | | | |  __/
#      \____/ \__,_|_| |_| |_|\___|
#     """
#     print(art)

# print_ascii_art()

## using a libray known as pyfiglet
# pip install pyfiglet
# import pyfiglet

# def print_ascii_art(text):
#     ascii_art = pyfiglet.figlet_format(text)
#     print(ascii_art)

# if __name__ == "__main__":
#     print_ascii_art("Hello, World!")


# pip install pillow
## using an image
# from PIL import Image

# def image_to_ascii(image_path, width=100):
#     image = Image.open(image_path)
#     aspect_ratio = image.height / image.width
#     new_height = int(aspect_ratio * width)
#     image = image.resize((width, new_height))
#     image = image.convert("L")  # Convert to grayscale

#     pixels = image.getdata()
#     ascii_chars = "@%#*+=-:. "
#     ascii_str = ''.join([ascii_chars[pixel // 32] for pixel in pixels])
    
#     ascii_str = '\n'.join([ascii_str[i:i + width] for i in range(0, len(ascii_str), width)])
#     return ascii_str

# def print_image_ascii(image_path):
#     ascii_art = image_to_ascii(image_path)
#     print(ascii_art)

# if __name__ == "__main__":
#     print_image_ascii("example_image.png")  # Replace with your image file path

