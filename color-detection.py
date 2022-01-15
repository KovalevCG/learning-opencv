import cv2
import numpy as np

path = 'assets/pickup.jpg'
img = cv2.imread(path)

x = int(img.shape[0]/2)
y = int(img.shape[1]/2)

img = cv2.resize(img, (y ,x))

cv2.imshow("Image", img)
cv2.waitKey()