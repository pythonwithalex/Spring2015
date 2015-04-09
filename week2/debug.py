#!/usr/bin/env python
'''
  random_string(N) --> random string of length N
'''

import random

# notes on the funcs we use:
#  random.randrange -> gives you a random integer in range(M,N-1)
#  chr -> turns a number into an ASCII character


# Assignment: this function works pretty well, but it isn't perfect, nor very safe
# 1) see if you can figure out why by testing various input on it
# 2) finally, add code prevent unexpected errors

def random_string(length):
  random_string = ''
  while length:
    random_string += chr(random.randrange(97,123))
    length -= 1
  return random_string
  
print 'a random string of length 8: {}'.format(random_string(8))
