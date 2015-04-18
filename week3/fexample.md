````python

import random

def gen_sample_space():
  '''
    a list of strings to choose from when generating a pseudo-random string
  '''
  return ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def gen_random_string(n,sspace):
  if n < 1:
    return ''
  resulting_string = ''
  while n:
    resulting_string = resulting_string + random.choice(sspace)
    n = n - 1
  return resulting_string

def main():
  sample_space = gen_sample_space()
  print gen_random_string(0, sample_space)

main()
````
