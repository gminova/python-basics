class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
print(felix.color)


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()


class Doggo:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color


fido = Doggo("Fido", "brown")
print(fido.legs)
print(Doggo.legs)
