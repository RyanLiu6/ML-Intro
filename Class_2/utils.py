import cv2

class pyImage:
    def __init__(self, imageName):
        self.imageName = imageName
        self.imageMat = cv2.imread(imageName, cv2.IMREAD_UNCHANGED)
