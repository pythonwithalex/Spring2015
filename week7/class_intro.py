#!/usr/env/bin python
# An introductory example to Object Oriented Programming

from math import pi

# here I will define a Shape class, a circle class and a square class.  
# The circle and square classes inherit the qualities of the shape class

class Shape(object):

  name = 'general shape'

  def speak(self):
    print "Hello, I am a {}.".format(self.name)


class Circle(Shape):

  name = 'circle'

  def __init__(self,radius):
    self.radius = radius

  def get_circumference(self):
    diameter = 2 * self.radius
    return diameter*pi

  def get_area(self):
    return (self.radius**2) * pi


class Square(Shape):

  name = 'square'

  def __init__(self,side):
    self.side = side

  def get_area(self):
    return self.side**2


# now I will create objects out of the classes defined above

circle = Circle(5)
circle.speak()
print circle.radius
print circle.get_circumference()
print circle.get_area()

square = Square(4)
square.speak()
print square.side
print square.get_area()
print circle.radius
print circle.radius
