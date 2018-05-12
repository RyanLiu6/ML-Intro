import extraction as ex
import utils

label = "label.png"
tree = "tree.jpg"

def main():
#     ex.imageToString(label)

    tuner = utils.imageTuner()
    tuner.tuneContrast(utils.pyImage(tree), 1)


if __name__ == "__main__":
    main()
