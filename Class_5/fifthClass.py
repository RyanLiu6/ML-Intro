import extraction as ex


def main():
    loopCondition = True
    while loopCondition:
        print("Press 0 to quit.")
        select = input("Or Press any key to continue.\n")

        if select is "0":
            loopCondition = False
            print("Goodbye!")
        else:
            imageName = input("Please enter the path to the Image:\n")

            ex.imageToString(imageName)


if __name__ == "__main__":
    main()
