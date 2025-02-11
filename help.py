class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Sound")

class Dog(Animal):
    def sound(self):
        print("wow - wow")

class Cat(Animal):
    def sound(self):
        print("Miaow")

d = Dog("A")
d.sound()

c = Cat("M")
c.sound()