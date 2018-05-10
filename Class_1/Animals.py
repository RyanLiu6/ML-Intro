import Animal as am

class Dog(am.Animal):
    def __init__(self):
        super.__init__

    def doAction(self):
        print(self.name + " wags their tag")


class Cat(am.Animal):
    pass
