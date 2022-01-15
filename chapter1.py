import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(3, 480)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (320,240))
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
