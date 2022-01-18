import cv2
import numpy as np


def empty(a):
    pass


def find_color(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    if mask_test:
        h_min = cv2.getTrackbarPos("Hue Min", "Settings")
        h_max = cv2.getTrackbarPos("Hue Max", "Settings")
        s_min = cv2.getTrackbarPos("Sat Min", "Settings")
        s_max = cv2.getTrackbarPos("Sat Max", "Settings")
        v_min = cv2.getTrackbarPos("Val Min", "Settings")
        v_max = cv2.getTrackbarPos("Val Max", "Settings")
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
    else:
        lower = np.array(color_masks[0][0:3])
        upper = np.array(color_masks[0][3:6])
    mask = cv2.inRange(img_hsv, lower, upper)
    # cv2.imshow("img", mask)
    x, y = get_contours(mask)

    if (x != 0) and (y != 0):
        if paint_bool:
            cv2.circle(img_canvas, (x, y), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img_result, (x, y), 10, (0, 255, 0), 2)
        cv2.imshow("canvas", img_canvas)


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            # cv2.drawContours(img_result, cnt, -1, (0, 0, 255), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            obj_corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
    return (x + w // 2), y


color_masks = [[72, 39, 196, 93, 145, 255],
               [72, 93, 39, 145, 196, 255]]

mask_test = False
paint_bool = False

# Trackbars
if mask_test:
    cv2.namedWindow("Settings")
    cv2.resizeWindow("Settings", 340, 240)
    cv2.createTrackbar("Hue Min", "Settings", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "Settings", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "Settings", 0, 255, empty)
    cv2.createTrackbar("Sat Max", "Settings", 255, 255, empty)
    cv2.createTrackbar("Val Min", "Settings", 0, 255, empty)
    cv2.createTrackbar("Val Max", "Settings", 255, 255, empty)

cap = cv2.VideoCapture(0)
img_canvas = np.zeros((480, 640, 3), np.uint8)


while True:
    _, img = cap.read()
    img_result = img.copy()
    find_color(img)
    img_result = cv2.bitwise_or(img_result, img_canvas)
    cv2.imshow("WebCamContours", img_result)
    k = cv2.waitKey(1)
    if k & 0xFF == ord('p'):
        paint_bool = np.invert(paint_bool)
        print(paint_bool)
    if k & 0xFF == ord('e'):
        img_canvas = np.zeros((480, 640, 3), np.uint8)
    if k & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

