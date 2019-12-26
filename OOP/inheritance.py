class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()


class Wolf:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def bark(self):
        print('Grr...')


class Dog(Wolf):
    def bark(self):
        print('Awoooo')


husky = Dog('max', 'grey')
husky.bark()
