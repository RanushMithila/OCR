import pytesseract
import PIL.Image
import cv2


ocrConfig = r'--psm 3 --oem 3'

text = pytesseract.image_to_string(
    PIL.Image.open('img/1.jpg'), config=ocrConfig)

print(text)
