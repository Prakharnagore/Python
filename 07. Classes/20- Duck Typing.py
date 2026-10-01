def make_it_speak(animal):
    animal.speak()


class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


class Human:
    def speak(self):
        print("Hello")


make_it_speak(Dog())
make_it_speak(Cat())
make_it_speak(Human())
