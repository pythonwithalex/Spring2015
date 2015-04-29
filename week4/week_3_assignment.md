## This Week's Assignment

#### Functions Exercise

+ Write a program that doubles the square of a third of the reverse of the str() of the max of this list: [01,94,30,3.0,53].

+ For this problem, you should break this down into discrete steps and write a function to solve each part in isolation.  Then call them in a way that ensures the data from one is passed to the next relevant function (hint, use 'return').  Breaking a problem into many functions also ensures that you can test that each function works in isolation ( called a 'unit test'), and then you can have a better idea of what is going wrong when you call main().

+ Here's a self-contained proof-of-concept example in which I generate a pseudo-random string of a specified length using a  function to generate the characters for the string, a function that generates a string from the characters in the previous function, and a main function that calls these two functions.  Notice the definitions come first and the main call() is at the very bottom.

```python 

import random

def gen_sample_space():
  '''
    a list of strings to choose from when generating a pseudo-random string
  '''
  return ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def gen_random_string(n,sspace):
  '''
    gen_random_string(n,sspace) -> pseudo-random string of length n, using chars from sample space.
  '''
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
