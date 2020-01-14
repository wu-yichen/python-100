import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute(self):
        return self.radius ** 2 * math.pi


circle = Circle(2)
print(circle.compute())
