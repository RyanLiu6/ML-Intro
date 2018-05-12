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
        blue, green, red = cv2.split(temp)

        blue *= 0.299
        green *= 0.587
        red *= 0.114

        lumin = blue + green + red
        # https://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color


class imageTuner:
    maxPixel = 255
    def tuneBrightness(self, image, brightness):
        # Brightness is Beta Channel
        self.alpha = 1
        self.beta = brightness
        self.image = image
        self.tuneHelper(image)

    def tuneContrast(self, image, contrast):
        # Contrast is Alpha Channel
        self.alpha = contrast
        self.beta = 0
        self.image = image
        self.tuneHelper(image)

    def tuneHelper(self, image):
        shape = image.imageMat.shape
        newImage = np.zeros((shape[0], shape[1]), image.imageMat.dtype)

        cv2.imwrite(os.path.join(ABSPATH, "changed_" + image.imageName), newImage)

    def transform(self, inputPixel):
        return (inputPixel - 0.5)*alpha + 0.5 + beta
