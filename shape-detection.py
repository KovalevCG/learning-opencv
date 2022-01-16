import cv2

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(imgContours, (x, y), (x + w, y + h), (100, 220, 65), 4)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1:
            # cv2.drawContours(imgContours, cnt, -1, (100, 220, 65), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            obj_corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if obj_corners == 3:
                obj_type = 'Triangle'
            elif obj_corners == 4:
                aspect_ratio = w / float(h)
                if (aspect_ratio > 0.95) and (aspect_ratio < 1.05):
                    obj_type = "Square"
                else:
                    obj_type = "Rectangle"
            elif obj_corners == 5:
                obj_type = "Pentagon"
            else:
                obj_type = 'Circle'
            print(area, peri, obj_corners)
            # cv2.rectangle(imgContours, (x, y), (x + w, y + h), (100, 220, 65), 4)
            # cv2.putText(imgContours, obj_type,
            #             (x+5, y-22+5), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 5)
            cv2.putText(imgContours, obj_type,
                        (x+5, y-22+5), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 0), 2)

path = 'assets/shapes2.png'
img = cv2.imread(path)
imgContours = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

imgCanny = cv2.Canny(imgBlur, 150, 150)
getContours(imgCanny)
imgContours = cv2.resize(imgContours, (800, 600), interpolation=cv2.INTER_AREA)
cv2.imshow('Image', imgContours)
cv2.waitKey(0)