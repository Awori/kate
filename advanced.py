#superclass 
class Shape:
#constructor __init__ method
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height   

rectangle = Rectangle("red", 5, 7)
print(rectangle.get_color())  # Output: red
print(rectangle.area())  # Output: 35    