# Use comparison magic methods to compare objects
# Link to the documentation: https://docs.python.org/3/reference/datamodel.html#special-method-names

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point1 = Point(10, 20)
point2 = Point(1, 2)
# without __eq__ method, we can't compare objects
print(point1 == point2)  # False
# with __eq__ method, we can compare objects
print(point1 == point2)  # True
# with __gt__ method, we can compare objects
print(point1 > point2)  # True
