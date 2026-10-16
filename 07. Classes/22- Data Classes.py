from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(1, 2)
# Different ids because we are creating two different objects -> Different memory addresses
print(id(p1))
# Different ids because we are creating two different objects -> Different memory addresses
print(id(p2))

# False because we are comparing two different objects -> Different memory addresses
print(p1 == p2)


# Using namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
# Same ids because we are creating two different objects with the same values -> Same memory addresses
print(id(p1))
# Same ids because we are creating two different objects with the same values -> Same memory addresses
print(id(p2))

# True because we are comparing two different objects with the same values -> Same memory addresses
print(p1 == p2)

print(p1.x)
print(p1.y)
