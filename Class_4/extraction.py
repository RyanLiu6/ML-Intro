import os
import cv2
import utils

import pytesseract as smt


MOD = "Modified"
OUT = "Output/"
ABSPATH = os.path.dirname(os.path.realpath(__file__))

userInfo = {}
packageInfo = []

thresh = 150


def imageToString(imagefile):
    # Given a path to the image, oppen it as a pyImage object
    image = utils.pyImage(imagefile)

    print(image.imageMat.shape)

    currImage = cleanImage(image)
    outputStr = smt.image_to_string(currImage, lang="eng")

    with open(os.path.join(ABSPATH, OUT, "test.txt"), "wb") as f:
        f.write(outputStr.encode("utf-8"))
