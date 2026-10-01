class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print("fly")


m = Mammal()
print(m.age)  # Error: 'Mammal' object has no attribute 'age'
print(m.weight)  # 2

# Using super() to call the parent class constructor
print(m.age)  # 1
print(m.weight)  # 2
