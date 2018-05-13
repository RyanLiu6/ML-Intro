import os
import cv2
import utils
import checker

import pytesseract as smt


OUT = "Output/"
ABSPATH = os.path.dirname(os.path.realpath(__file__))

cleaner = utils.imageCleaner()
tuner = utils.imageTuner()
checker = checker.packageChecker()

userInfo = {
    "Name": "Ryan Liu",
    "Phone": "123-456-7890",
    "Email": "123@123.com",
    "Address": "MCLD 112"
}

packageInfo = [
    {
      "Package Name": "New Phone",
      "Shipping Company": "Amazon",
      "Tracking Info": "123-456-7890",
      "Delivery Date": "04/20/2018"
    },
    {
      "Package Name": "Nintendo Switch",
      "Shipping Company": "Amazon",
      "Tracking Info": "123-456-7890",
      "Delivery Date": "05/13/2018"
    }
]


def imageToString(imagefile):
    # Given a path to the image, oppen it as a pyImage object
    image = utils.pyImage(imagefile)

    currImage = cleaner.clean(image)
    outputStr = smt.image_to_string(currImage, lang="eng")

    with open(os.path.join(ABSPATH, OUT, "test.txt"), "wb") as f:
        f.write(outputStr.encode("utf-8"))

    print("***********************")
    print(outputStr)
    print("***********************")

    splitStr = outputStr.splitlines()

    user = checker.checkUser(splitStr, userInfo)
    delivery = checker.checkPackage(splitStr, packageInfo)

    print("="*40)
    print("User:     {}".format(user))
    print("Delivery: {}".format(delivery))

    if user and delivery:
        print("There's a match!")
    else:
        print("No match!")
