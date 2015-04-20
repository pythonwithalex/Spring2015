#!/usr/bin/env python

# get a third of the square of half of the reverse of the str() of the max of this list [01,22,1,1.00,4,-20]

# decorator for int conversion if necessary?

def string_to_float(func):
  def inner(n):
    if type(n) is str:
      return func(float(n))
  return inner
 
def squareof(n):
  return n*n

def thirdof(n):
  return n/3.0

@string_to_float
def halfof(n):
  return n/2.0

def reverse(s):
  return s[::-1]


data = [01,22,1,1.00,4,-20]
function_stack = [max,str,reverse,halfof,squareof,thirdof]
function_stack.reverse()

temp = data 
while len(function_stack):
  this_func = function_stack.pop()
  temp = this_func(temp)
  print temp
