class Point:
    # Instance method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Class method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Drawing point at ({self.x}, {self.y})")


point = Point.zero()
print(point)  # <__main__.Point object at 0x7f5985490550>

point.draw()  # Draws the point at (0, 0)
