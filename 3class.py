class Grandparent:
    height = 170
    gladness = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print(self.height)
        print(self.gladness)
        print(self.age)

kira = Child()