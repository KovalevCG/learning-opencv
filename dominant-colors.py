import cv2
import numpy as np


def create_bar(bar_height, bar_width, color):
    bar = np.zeros((bar_height, bar_width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)


def nothing(x):
    global trackbar_changed
    trackbar_changed = True


# Global Variables
trackbar_changed = False

# Trackbar
cv2.namedWindow("Settings")
cv2.createTrackbar("Number", "Settings", 3, 10, nothing)

original = cv2.imread("assets/lp-city.jpg")
# original = cv2.imread("assets/forest.jpg")
# original = cv2.imread("assets/pickup.jpg")
resize = original.copy()
resize_width = 600
height, width = original.shape[:2]
resize = cv2.resize(original, (resize_width, (resize_width * height) // width))
height, width = resize.shape[:2]

# Reshape image for kmeans
data = np.reshape(resize, (height*width, 3))
data = np.float32(data)

# Main Loop
while True:
    # If amount of colors was changed
    if trackbar_changed:
        number_clusters = cv2.getTrackbarPos("Number", "Settings")
        if number_clusters < 2:
            number_clusters = 2
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        flags = cv2.KMEANS_RANDOM_CENTERS
        compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)

        bars = []
        rgb_values = []

        for index, row in enumerate(centers):
            bar, rgb = create_bar(70, 70, row)
            bars.append(bar)
            rgb_values.append(rgb)

        img_bar = np.hstack(bars)
        trackbar_changed = False

        cv2.imshow("Image", resize)
        cv2.imshow("Bar", img_bar)

    # Exit if "Esc" pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
