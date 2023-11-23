
import numpy as np
import easyocr
import imutils
import cv2
from matplotlib import pyplot as pl 

img = cv2.imread('images/plate_1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200 )

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key = cv2.contourArea, reverse = True)[:8]

pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 10, True)
    if len(approx) == 4:
        pos = approx
        break

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img,img, mask = mask)

(x, y) = np.where(mask == 255)
(x1, y1 )= (np.min(x), np.min(y))
(x2, y2) = (np.min(x), np.min(y))


pl.imshow(cv2.cvtColor(bitwise_img, cv2.COLOR_BGR2RGB))
pl.show()