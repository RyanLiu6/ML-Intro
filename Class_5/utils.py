import os
import cv2
import numpy as np

thresh = 150

ABSPATH = os.path.dirname(os.path.realpath(__file__))

class pyImage:
    def __init__(self, imageName):
        self.imageName = imageName
        self.imageMat = cv2.imread(imageName, cv2.IMREAD_UNCHANGED)


class imageCleaner:
    def clean(self, image):
        # Check Brightness and change Threshold filter
        # self.checkBrightness(image)

        # Convert image to Grayscale
        grayScale = cv2.cvtColor(image.imageMat, cv2.COLOR_RGB2GRAY)

        #absPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), MOD)

        cv2.imwrite(os.path.join(ABSPATH, "grayscale_" + image.imageName), grayScale)

        # Strict Threshold based on a value we manually set
        # self.__strictThresh__(grayScale)

        # Adaptive Threshold using OpenCV Methods
        self.__adaptiveThresh__(grayScale)

        # Denoise image
        grayScale = cv2.fastNlMeansDenoising(grayScale, 10, 10, 7, 21)

        cv2.imwrite(os.path.join(ABSPATH, "cleaned_" + image.imageName), grayScale)

        return grayScale

    def __strictThresh__(self, image):
        # Apply threshold to get true Binary represenation of image
        ret, grayScale = cv2.threshold(grayScale, thresh, 255, cv2.THRESH_BINARY)

    def __adaptiveThresh__(self, image):
        image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)


class imageTuner:
    # https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv
    # http://pippin.gimp.org/image_processing/chap_point.html
    # https://stackoverflow.com/questions/32609098/how-to-fast-change-image-brightness-with-python-opencv
    def tuneBrightness(self, image, brightness):
        # Brightness is Beta Channel
        # Choose between 0 - 100
        self.alpha = 1
        self.beta = brightness
        self.__tuneHelper__(image)

    def tuneContrast(self, image, contrast):
        # Contrast is Alpha Channel
        # Choose between -127 to 127
        self.alpha = contrast
        self.beta = 0
        self.__tuneHelper__(image)

    def tuneBoth(self, image, contrast, brightness):
        self.alpha = contrast
        self.beta = brightness
        self.__tuneHelper__(image)

    def __tuneHelper__(self, image):
        # Convert to signed 16 bit to allow for < 0 and > 255
        temp = np.int16(image.imageMat)

        print(self.alpha)
        print(self.beta)

        # Apply contrast and brightness adjustments
        temp = temp*(self.alpha/127 + 1) - self.alpha + self.beta

        # Restrict to between 0 and 255
        temp = np.clip(temp, 0, 255)

        # Convert back to unsigned 8bit int
        temp = np.uint8(temp)

        cv2.imwrite(os.path.join(ABSPATH, "tuned_" + image.imageName), temp)
