#!/usr/env/bin python

from math import pi

class Shape(object):

  name = 'general shape'

  def speak(self):
    print "Hello, I am a {}.".format(self.name)


class Circle(Shape):

  name = 'circle'

  def __init__(self,radius):
    self.radius = radius

  def speak(self):
    print "I am a {}.".format(self.name)

  def get_circumference(self):
    diameter = 2 * self.radius
    return diameter*pi

  def get_area(self):
    return (self.radius**2) * pi


class Square(Shape):

  name = 'square'

  def __init__(self,side):
    self.side = side

  def speak(self):
    print "I am a {}".format(self.name)

  def get_area(self):
    return self.side**2

circle = Circle(5)
print circle.radius
print circle.get_circumference()
print circle.get_area()
