## 1: Which line in list 2 causes its output to differ from list 1 ?

````python
l = [num for num in range(4)]
l.append('four')
l.extend([5.0,6])
l += ['7',16/2,[9,10]]
print l
````

````python
y = []
y.extend(range(3))
y.append(['four',5.0])
y += [6,'7',8,[9,10]]
print y
````

## 2: find the sum of all even numbers under 100 that contain a '4' or a '2'

## 3: Swap Values 

The function below takes in two arguments and swaps their values.  However, it is missing the actual code that does the swap.  Write that code, leaving the rest of the function unchanged.

````python
def swap(num_a, num_b):

  # your code goes here
  return a,b

````

## 4: Writing a wrapper function for id()

The id() function returns an integer that represents the location (memory address) of an object in python.  Here's an example:

````python

a = 'me'
b = 'you'

print id(a)
# prints 3252448
print id(b)
# prints 7646720
````

It is useful, but we could make the information given by the id() function easier if we truncate the number so that only the last N digits are shown.

Write a function that takes in one positive integer, N, and returns the last N digits of the memory address.  You should use the id() function in your function.  If the integer N is larger than the size of the number id() returns, then just return the results of id().
