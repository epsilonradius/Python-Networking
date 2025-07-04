import pytesseract
from PIL import Image

    # Set the path to the Tesseract executable (replace with your actual path)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

    # Open the image using Pillow
image_path = r"C:\Users\david\Documents\PowerShell\Scripts\work\tf\cropped\20210616_110912_c.jpg"
img = Image.open(image_path)

    # Use pytesseract to extract text
text = pytesseract.image_to_string(img)

    # Print the extracted text
print(text)