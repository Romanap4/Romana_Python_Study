# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods.

# ternary operator? 

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# method overwriting ˇˇˇ ; is a child shares a similar method with the parent, the child method will be used

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
#         self.color = color
#         self.filled = filled
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()                  # extending the functionality of the describe method; the order doesn't matter
        

class Square(Shape):
    def __init__(self, color, is_filled, width):
#         self.color = color
#         self.filled = filled
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
#         self.color = color
#         self.filled = filled
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()

# shared attributes will be placed within a parent (super) class to increase maintainability

# you can use the keyword arguments for better readability, but it's not necessary
circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

circle.describe()
square.describe()
triangle.describe()

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

