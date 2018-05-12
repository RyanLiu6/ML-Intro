import cv2

thresh = 150

class pyImage:
    def __init__(self, imageName):
        self.imageName = imageName
        self.imageMat = cv2.imread(imageName, cv2.IMREAD_UNCHANGED)


class imageCleaner:
    def clean(self, image):
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

    def getBrightness(self, image):
        temp = image.imageMat
        blue, green, red = cv2.split(temp)

        blue *= 0.299
        green *= 0.587
        red *= 0.114

        lumin = blue + green + red
        # https://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color


class imageTuner:
    pass
