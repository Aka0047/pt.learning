import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
# Path to tesseract executable (not needed if Tesseract is in your PATH)
# For Windows, it might look like this: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# For Linux and macOS, this is usually not required

# Replace 'path_to_image.jpg' with your image file path
image_path = 'deneme4.jpg'

# Open an image using Pillow
image = Image.open(image_path)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

print(text)