import cv2
import PIL.Image
import pytesseract
from pytesseract import Output


ocrConfig = r'--psm 3 --oem 3'

img = cv2.imread('img/address1.jpg')
height, width, _ = img.shape
data = pytesseract.image_to_data(
    img, config=ocrConfig, output_type=Output.DICT)

amountOfBox = len(data['text'])

for i in range(amountOfBox):
    if float(data['conf'][i]) > 80:
        (x, y, width, height) = (data['left']
                                 [i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(
            img, (x, y), (x + width, y + height), (0, 255, 0), 2)    # color BGR
        img = cv2.putText(img, data['text'][i],
                          (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

# print(data['text'])


cv2.imshow("Image", img)
cv2.waitKey(0)
