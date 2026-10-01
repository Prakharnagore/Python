class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("fly")


m = Mammal()
m.eat()
m.walk()
print(m.age)

isinstance(m, Mammal)  # True
isinstance(m, Animal)  # True
isinstance(m, object)  # True

issubclass(Mammal, Animal)  # True
issubclass(Animal, Mammal)  # False
issubclass(Mammal, object)  # True
issubclass(Animal, object)  # True
