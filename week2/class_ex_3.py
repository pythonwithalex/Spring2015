#!/usr/bin/env python
'''
  random_string(N) --> random string of length N
'''

import random

# notable built-ins:
#  random.randrange -> gives you a random integer in range(M,N-1)
#  chr -> turns a number into an ASCII character

def random_string(length):
  random_string = ''
  while length:
    random_string += chr(random.randrange(97,123))
    length -= 1
  return random_string
  
print 'a random string of length 8: {}'.format(random_string(8))
