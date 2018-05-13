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

        # Apply threshold to get true Binary represenation of image
        ret, grayScale = cv2.threshold(grayScale, thresh, 255, cv2.THRESH_BINARY)

        # Denoise image
        grayScale = cv2.fastNlMeansDenoising(grayScale, 10, 10, 7, 21)

        cv2.imwrite(os.path.join(ABSPATH, "cleaned_" + image.imageName), grayScale)

        return grayScale

    def checkBrightness(self, image):
        temp = image.imageMat
        shape = image.imageMat.shape
        blue, green, red = cv2.split(temp)

        blue *= 0.299
        green *= 0.587
        red *= 0.114

        lumin = blue + green + red
        # https://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color

        res = numpy.sum(lumin, axis = 0)
        brightness = res[0] / (255*shape[0]*shape[1])*2
        print(brightness)


class imageTuner:
    # https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv
    # http://pippin.gimp.org/image_processing/chap_point.html
    # https://stackoverflow.com/questions/32609098/how-to-fast-change-image-brightness-with-python-opencv
    def tuneBrightness(self, image, brightness):
        # Brightness is Beta Channel
        self.alpha = 1
        self.beta = brightness
        self.tuneHelper(image)

    def tuneContrast(self, image, contrast):
        # Contrast is Alpha Channel
        self.alpha = contrast
        self.beta = 0
        self.tuneHelper(image)

    def tuneHelper(self, image):
        # Convert to signed 16 bit to allow for < 0 and > 255
        temp = np.int16(image.imageMat)

        # Apply contrast and brightness adjustments
        temp = temp*(alpha/127 + 1) - alpha + beta

        # Restrict to between 0 and 255
        temp = np.clip(temp, 0, 255)

        # Convert back to unsigned 8bit int
        temp = np.uint8(temp)

        cv2.imwrite(os.path.join(ABSPATH, "tuned_" + image.imageName), temp)
