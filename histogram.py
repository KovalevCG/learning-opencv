import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("assets/lp-city.jpg")
img = cv2.resize(img, (700, 712))
cv2.imshow("Image", img)
cv2.waitKey(0)