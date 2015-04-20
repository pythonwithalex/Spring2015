#!/usr/bin/env python

# get a third of the square of half of the reverse of the str() of the max of this list [01,22,1,1.00,4,-20]

# decorator for str to float conversion
def string_to_float(func):
  def inner(n):
    if type(n) is str:
      return func(float(n))
  return inner

# decorator for  float to string conversion
# try turnary here
def float_to_str(func):
  def inner(n):
    if type(n) in [int,float]:
      return str(n)
    else:
      return n
  return inner

def tostr(n):
  return str(n) if type(n) is not str else n

def toint(n):
  return int(n) if type(n) is not int else n

def squareof(n):
  return n*n

def thirdof(n):
  return n/3.0

def halfof(n):
  return n/2.0

def reverse(s):
  return s[::-1]

data = [01,22,1,1.00,4,-20]
result = data
function_stack = [max,tostr,reverse,toint,halfof,squareof,thirdof]
function_stack.reverse()

while function_stack:
  f = function_stack.pop()
  result = f(result)

print result
