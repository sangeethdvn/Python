# Create a  class Rectsngle

# method1 = length and breadth

# method2 = parameter

# method3 = area

class Rectangle:

    def __init__(self, length, breadth):

        self.length = length

        self.breadth = breadth

        parameter = 2 * (self.breadth + self.length)

        self.parameter = parameter

        print(f"Paramter : {self.parameter}")


    def area(self):

        print(self.length * self.breadth)

obj = Rectangle(length=10, breadth=5)           #__init__/ constuctor

obj.area()