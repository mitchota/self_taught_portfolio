# Self-Taught Programming Assignment 6 - Inheritance

class Shape():
    def what_am_i(self):
        print("I am a shape.")
 
 
class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
 
    def calculate_perimeter(self):
        return 2 * self.length + 2 * self.width
 
class Square(Shape):
    def __init__(self, s):
        self.s1 = s
        
    def calculate_perimeter(self):
        return 4 * self.s1
    
    def change_size(self, g):
        self.s1 = self.s1 + g
 
box1 = Rectangle(5, 3)
box1.what_am_i()
 
box2 = Square(16)
box2.what_am_i()