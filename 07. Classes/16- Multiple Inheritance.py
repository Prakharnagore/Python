class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


m = Manager()

# Employee Greet - It prints the greet method of the Employee class because it is the first class in the inheritance chain.
# If there is no method in the Employee class, it will print the greet method of the Person class.
m.greet()
