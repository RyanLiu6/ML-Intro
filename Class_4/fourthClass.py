import extraction as ex
import utils

label = "label.png"
tree = "tree.jpg"

cleaner = utils.imageCleaner()
tuner = utils.imageTuner()

def main():
    ex.imageToString(label)

    treeImage = utils.pyImage(tree)
    # tuner.tuneBoth(treeImage, 64, 50)


if __name__ == "__main__":
    main()
