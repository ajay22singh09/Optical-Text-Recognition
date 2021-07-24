import pytesseract
from PIL import Image

def ocr_core(filename):
   

    # Load the image as a PIL/Pillow image, apply OCR and preprocessing technique and then delete the temporary file ................
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename))
    return text


