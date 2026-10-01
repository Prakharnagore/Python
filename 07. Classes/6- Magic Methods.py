# Magic methods are special methods that are called by the interpreter
# Link to the documentation: https://docs.python.org/3/reference/datamodel.html#special-method-names


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Magic method for string representation
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
print(point)  # (1, 2) - No need to call __str__ method, it's called automatically
print(str(point))  # (1,2) - same result
