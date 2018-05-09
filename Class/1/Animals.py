class Animal:
    # Base Class

    def __init__(self, name, height, weight, sound):
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound
        self.friends = {}

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getName(self):
        return self.name

    def getSound(self):
        return self.sound
