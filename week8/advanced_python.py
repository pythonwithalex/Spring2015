#!/usr/bin/env python

# splat operator
card = ('Queen','Spades')
#print "{} of {}".format(card[0],card[1])
#print "{} of {}".format(*card)

# *args, **kwargs
# 
# def print_args(*args):
#   for arg in args:
#     print arg
# print_args('one','two','three',5,None,'abc')
# print_args('one','two')

#def print_kwargs(**kwargs):
#  for k in kwargs:
#    print k

#l = [ ('b',4), ('a',2), ('b',0), ('b',-3) ]

#def custom_sort(t):
#  return t[0],t[1]
  
#print sorted(l,key=custom_sort)
#print sorted(l,key=lambda x: (x[0],x[1]))











# LOCAL, ENCLOSED, GLOBAL, BUILT-IN


def outer():

  phrase = 'is the coolest.'

  def inner(name):
    print ' '.join([name,phrase])
  return inner


sentence_generator = outer()
sentence_generator('Michael Jordan')

  



    


