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


class Doggy(Wolf):
    def bark(self):
        print('Awoooo')


husky = Doggy('max', 'grey')
husky.bark()


class A:
    def method(self):
        print("A method")


class B(A):
    def another_method(self):
        print("B method")


class C(B):
    def third_method(self):
        print("C method")


c = C()
c.method()
c.another_method()
c.third_method()


class M:
    def spam(self):
        print(1)


class N(M):
    def spam(self):
        print(2)
        super().spam()


N().spam()
