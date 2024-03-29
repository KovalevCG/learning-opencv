import cv2
import numpy as np

# Empty function for Trackbars
def empty(a):
    pass

# Reading Image
path = 'assets/menu.jpg'
img = cv2.imread(path)

# Trackbars
cv2.namedWindow("Settings")
cv2.resizeWindow("Settings", 340, 240)
cv2.createTrackbar("Hue Min", "Settings", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Settings", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Settings", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Settings", 255, 255, empty)
cv2.createTrackbar("Val Min", "Settings", 0, 255, empty)
cv2.createTrackbar("Val Max", "Settings", 255, 255, empty)

# Downscaling Original Image
x = int(img.shape[0]/3)
y = int(img.shape[1]/3)
img = cv2.resize(img, (y ,x))

# Main cycle
while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Settings")
    h_max = cv2.getTrackbarPos("Hue Max", "Settings")
    s_min = cv2.getTrackbarPos("Sat Min", "Settings")
    s_max = cv2.getTrackbarPos("Sat Max", "Settings")
    v_min = cv2.getTrackbarPos("Val Min", "Settings")
    v_max = cv2.getTrackbarPos("Val Max", "Settings")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Original", img)
    cv2.imshow("Mask", imgResult)
    cv2.imshow("BW Mask", mask)
    cv2.waitKey(1)