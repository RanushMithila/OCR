import pytesseract
import PIL.Image


ocrConfig = r'--psm 11 --oem 3'

text = pytesseract.image_to_string(
    PIL.Image.open('img/1.jpg'), config=ocrConfig)

print(text)
