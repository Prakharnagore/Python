from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(id(p1))
print(id(p2))

print(p1 == p2)


# Using namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(id(p1))
print(id(p2))

print(p1 == p2)

print(p1.x)
print(p1.y)
