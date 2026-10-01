class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


c = Chicken()
c.eat()
c.fly()


# Example of multi-level inheritance. This is not good because it is not a good design to inherit from multiple classes.
# Employee - Person - Mammal - Animal - Object
