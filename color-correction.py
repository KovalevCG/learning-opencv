import cv2
import numpy as np


def nothing(x):
    pass


def calculations(img, brightness=255, contrast=127, hue=127, saturation=127):

    # Recalculating the Values of the Trackbar Settings
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
    hue = int((hue - 0) * (127 - (-127)) / (254 - 0) + (-127))
    saturation = int((saturation - 0) * (127 - (-127)) / (254 - 0) + (-127))

    cal = img

    # Brightness Calculation
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255
        else:
            shadow = 0
            max = 255 + brightness
 
        al_pha = (max - shadow) / 255
        ga_mma = shadow
        cal = cv2.addWeighted(img, al_pha,
                              img, 0, ga_mma)

    # Contrast Calculation
    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
        cal = cv2.addWeighted(cal, Alpha,
                              cal, 0, Gamma)

    # Saturation Calculation
    saturation = saturation / 50.0
    if saturation != 1:
        calhsv = cv2.cvtColor(cal, cv2.COLOR_BGR2HSV).astype("float32")
        (h, s, v) = cv2.split(calhsv)
        s = s*saturation
        s = np.clip(s, 0, 255)
        cal = cv2.merge([h.astype("uint8"), s.astype("uint8"), v.astype("uint8")])
        cal = cv2.cvtColor(cal.astype("uint8"), cv2.COLOR_HSV2BGR)

    # Hue Calculation
    if hue != 0:
        calhsv = cv2.cvtColor(cal, cv2.COLOR_BGR2HSV).astype("float32")
        (h, s, v) = cv2.split(calhsv)
        h = h + hue
        cal = cv2.merge([h.astype("uint8"), s.astype("uint8"), v.astype("uint8")])
        cal = cv2.cvtColor(cal.astype("uint8"), cv2.COLOR_HSV2BGR)

    # Adding text string on the image
    cv2.putText(cal, 'B:{},C:{},S:{}'.format(brightness, contrast, saturation), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 5)
    cv2.putText(cal, 'B:{},C:{},S:{}'.format(brightness, contrast, saturation), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    return cal


if __name__ == '__main__':

    # Global Variables
    brightness = 0
    contrast = 0
    hue = 0
    saturation = 1

    # Image loading
    original = cv2.imread("./assets/van.jpg")

    # Image resizing
    original_height, original_width = original.shape[:2]
    resize_width = 640
    original = cv2.resize(original, (resize_width, int(resize_width * original_height / original_width)))
 
    # Making another copy of an image.
    img = original.copy()
 
    # Creating placeholder window
    cv2.namedWindow('Brightness/Contrast')

    # Brightness range -255 to 255
    cv2.createTrackbar('Brightness',
                       'Brightness/Contrast', 255, 2 * 255,
                       nothing)
    # Contrast range -127 to 127
    cv2.createTrackbar('Contrast', 'Brightness/Contrast',
                       127, 2 * 127,
                       nothing)
    # Hue range -127 to 127
    cv2.createTrackbar('Hue', 'Brightness/Contrast',
                       127, 2 * 127,
                       nothing)
    # Saturation range -127 to 127
    cv2.createTrackbar('Saturation', 'Brightness/Contrast',
                       177, 2 * 127,
                       nothing)

    while True:

        img = original.copy()

        # Get Trackbar Values
        brightness = cv2.getTrackbarPos('Brightness', 'Brightness/Contrast')
        contrast = cv2.getTrackbarPos('Contrast', 'Brightness/Contrast')
        hue = cv2.getTrackbarPos('Hue', 'Brightness/Contrast')
        saturation = cv2.getTrackbarPos('Saturation', 'Brightness/Contrast')

        # Calculate color correction based on trackbars
        effect = calculations(img, brightness,
                            contrast, hue, saturation)

        # Show final result
        cv2.imshow('Brightness/Contrast', effect)

        # Exit if "Esc" pressed
        key = cv2.waitKey(1)
        if key == 27:
            break

    # Closing cv2 windows
    cv2.destroyAllWindows()




