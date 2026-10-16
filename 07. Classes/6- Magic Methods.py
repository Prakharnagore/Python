# Magic methods are special methods that are called by the interpreter
# Link to the documentation: https://docs.python.org/3/reference/datamodel.html#special-method-names


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Magic method for string representation
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Magic method for addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point1 = Point(1, 2)
print(point1)  # (1, 2) - No need to call __str__ method, it's called automatically
print(str(point1))  # (1,2) - same result


point2 = Point(3, 4)
print(point1 + point2)  # (4, 6) - Addition of two points
