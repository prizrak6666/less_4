class Grandparent:
    def about(self):
        print("Я дідусь прикинь!!!!!!!")

    def about_me(self):
        print("Я бабуся ще хуже...")

class Parent(Grandparent):
    def about_me(self):
        print("Я батя!!!")

class Child(Parent):
    def __init__(self):
        super().about()
        super().aboout_me()

kira = Child()