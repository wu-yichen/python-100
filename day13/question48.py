class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute(self):
        return self.length * self.width


print(Rectangle(2, 3).compute())
