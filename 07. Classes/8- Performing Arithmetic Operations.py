# Use numeric magic methods to perform arithmetic operations
# Link to the documentation: https://docs.python.org/3/reference/datamodel.html#special-method-names

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point1 = Point(1, 2)
point2 = Point(3, 4)
print(point1 + point2)  # Point(4, 6)
