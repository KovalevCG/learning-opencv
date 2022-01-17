import cv2

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    cv2.imshow("video", img)
    k = cv2.waitKey(0)
    print(k)
    print(k&0xFF)