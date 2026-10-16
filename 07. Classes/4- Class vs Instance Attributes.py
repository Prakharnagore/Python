class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawing point at ({self.x}, {self.y})")


point = Point(1, 2)  # Instance attribute
print(point)  # <__main__.Point object at 0x7f5985490550>

point.draw()  # Drawing point at (1, 2)
print(point.default_color)  # red
print(Point.default_color)  # red
