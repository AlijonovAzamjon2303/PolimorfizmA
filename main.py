class Person:
    def __init__(self, name, fam):
        self.name = name
        self.fam = fam
    def hi(self):
        print("Hello")

class Englishman(Person):
    pass

class Uzbek(Person):
    def hi(self):
        super().hi()
        print("Assalomu alaykum")

u = Uzbek("A", "F")
u.hi()
# e = Englishman("A", "F")
# e.hi()