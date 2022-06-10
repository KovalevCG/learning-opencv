import cv2
import numpy as np
 
def BrightnessContrast(brightness=0):
    
    # getTrackbarPos returns the current
    # position of the specified trackbar.
    brightness = cv2.getTrackbarPos('Brightness', 'Brightness/Contrast')
     
    contrast = cv2.getTrackbarPos('Contrast', 'Brightness/Contrast')

    hue = cv2.getTrackbarPos('Hue', 'Brightness/Contrast')
    
    saturation = cv2.getTrackbarPos('Saturation', 'Brightness/Contrast')

    img = original.copy()

    effect = controller(img, brightness,
                        contrast, hue, saturation)
 
    # The function imshow displays an image
    # in the specified window
    cv2.imshow('Brightness/Contrast', effect)


def controller(img, brightness=255, contrast=127, hue = 127, saturation=127):
    print('brightness orig:', brightness)
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    print('brightness:', brightness)
 
    print('contrast orig:', contrast)
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
    print('contrast:', contrast)

    hue = int((hue - 0) * (127 - (-127)) / (254 - 0) + (-127))

    print('saturation orig:', saturation)
    saturation = int((saturation - 0) * (127 - (-127)) / (254 - 0) + (-127))
    print('saturation:', saturation)

    if brightness != 0:
 
        if brightness > 0:
 
            shadow = brightness
 
            max = 255
 
        else:
 
            shadow = 0
            max = 255 + brightness
 
        al_pha = (max - shadow) / 255
        ga_mma = shadow
 
        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(img, al_pha,
                              img, 0, ga_mma)
 
    else:
        cal = img
 
    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
 
        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(cal, Alpha,
                              cal, 0, Gamma)

    saturation = saturation / 50.0
    if saturation != 0:
        calhsv = cv2.cvtColor(cal, cv2.COLOR_BGR2HSV).astype("float32")
        (h, s, v) = cv2.split(calhsv)
        s = s*saturation
        s = np.clip(s,0,255)
        cal = cv2.merge([h.astype("uint8"),s.astype("uint8"),v.astype("uint8")])
        cal = cv2.cvtColor(cal.astype("uint8"), cv2.COLOR_HSV2BGR)

    if hue != 0:
        calhsv = cv2.cvtColor(cal, cv2.COLOR_BGR2HSV).astype("float32")
        (h, s, v) = cv2.split(calhsv)
        h = h + hue
        cal = cv2.merge([h.astype("uint8"),s.astype("uint8"),v.astype("uint8")])
        cal = cv2.cvtColor(cal.astype("uint8"), cv2.COLOR_HSV2BGR)

    # Creating text string in the image.
    cv2.putText(cal, 'B:{},C:{},S:{}'.format(brightness, contrast, saturation), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 5)
    cv2.putText(cal, 'B:{},C:{},S:{}'.format(brightness, contrast, saturation), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    return cal


if __name__ == '__main__':

    # Image loading
    original = cv2.imread("./assets/pickup.jpg")

    # Image resizing
    original = cv2.resize(original, (640, 480))
 
    # Making another copy of an image.
    img = original.copy()
 
    # Creating placeholder window
    cv2.namedWindow('Brightness/Contrast')

    # Brightness range -255 to 255
    cv2.createTrackbar('Brightness',
                       'Brightness/Contrast', 255, 2 * 255,
                       BrightnessContrast)
    # Contrast range -127 to 127
    cv2.createTrackbar('Contrast', 'Brightness/Contrast',
                       127, 2 * 127,
                       BrightnessContrast)
    # Hue range -127 to 127
    cv2.createTrackbar('Hue', 'Brightness/Contrast',
                       127, 2 * 127,
                       BrightnessContrast) 
    # Saturation range -127 to 127
    cv2.createTrackbar('Saturation', 'Brightness/Contrast',
                       127, 2 * 127,
                       BrightnessContrast) 

    while True:
        # Get trackbars values
        brightness = cv2.getTrackbarPos('Brightness', 'Brightness/Contrast')
        contrast = cv2.getTrackbarPos('Contrast', 'Brightness/Contrast')
        hue = cv2.getTrackbarPos('Hue', 'Brightness/Contrast')
        saturation = cv2.getTrackbarPos('Saturation', 'Brightness/Contrast')

        img = original.copy()

        print('brightness orig:', brightness)
        brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
        print('brightness:', brightness)

        print('contrast orig:', contrast)
        contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
        print('contrast:', contrast)

        hue = int((hue - 0) * (127 - (-127)) / (254 - 0) + (-127))

        print('saturation orig:', saturation)
        saturation = int((saturation - 0) * (127 - (-127)) / (254 - 0) + (-127))
        print('saturation:', saturation)

        if brightness != 0:

            if brightness > 0:

                shadow = brightness

                max = 255

            else:

                shadow = 0
                max = 255 + brightness

            al_pha = (max - shadow) / 255
            ga_mma = shadow

            # The function addWeighted calculates
            # the weighted sum of two arrays
            cal = cv2.addWeighted(img, al_pha,
                                  img, 0, ga_mma)

        else:
            cal = img

        if contrast != 0:
            Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
            Gamma = 127 * (1 - Alpha)

            # The function addWeighted calculates
            # the weighted sum of two arrays
            cal = cv2.addWeighted(cal, Alpha,
                                  cal, 0, Gamma)

        saturation = saturation / 50.0
        if saturation != 0:
            calhsv = cv2.cvtColor(cal, cv2.COLOR_BGR2HSV).astype("float32")
            (h, s, v) = cv2.split(calhsv)
            s = s * saturation
            s = np.clip(s, 0, 255)
            cal = cv2.merge([h.astype("uint8"), s.astype("uint8"), v.astype("uint8")])
            cal = cv2.cvtColor(cal.astype("uint8"), cv2.COLOR_HSV2BGR)

        if hue != 0:
            calhsv = cv2.cvtColor(cal, cv2.COLOR_BGR2HSV).astype("float32")
            (h, s, v) = cv2.split(calhsv)
            h = h + hue
            cal = cv2.merge([h.astype("uint8"), s.astype("uint8"), v.astype("uint8")])
            cal = cv2.cvtColor(cal.astype("uint8"), cv2.COLOR_HSV2BGR)

        # Creating text string in the image.
        cv2.putText(cal, 'B:{},C:{},S:{}'.format(brightness, contrast, saturation), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 5)
        cv2.putText(cal, 'B:{},C:{},S:{}'.format(brightness, contrast, saturation), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        # effect = controller(img, brightness,
        #                     contrast, hue, saturation)

        # The function imshow displays an image
        # in the specified window
        cv2.imshow('Brightness/Contrast', cal)

        cv2.waitKey(0)




