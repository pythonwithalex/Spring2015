max = 100
for i in range(1,max+1):
  if i%3 == 0 and i%5 == 0: # could also do 'if i%(3*5) == 0:'
    print "FizzBuzz"
  elif i%3 == 0:
    print "Fizz"
  elif i%5 == 0:
    print "Buzz"
  else:
    print i
