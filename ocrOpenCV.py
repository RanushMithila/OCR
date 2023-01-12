import pytesseract
import cv2


ocrConfig = r'--psm 3 --oem 3'

img = cv2.imread('img/logo.jpg')
height, width, _ = img.shape
boxes = pytesseract.image_to_boxes(img, config=ocrConfig)

for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(
        img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)    # color BGR

cv2.imshow("Image", img)
cv2.waitKey(0)
