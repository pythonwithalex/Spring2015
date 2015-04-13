## Loop 'equivalence'

#### While loop

````python

# assign the value zero to the name 'n'
n = 0

while n < 5:
  print n
  n = n + 1 # reassign the value of 1 greater than n to the name 'n'
  
````

#### For loop


````python

for n in range(5): # equivalent to 'for n in [1,2,3,4,5]:'
  print n

````

#### Questions:
+ In the while loop, why would it be a bad idea to print `n` on the last line of the loop?
+ What is the value of `n` after the for loop completes? after the while loop completes? Does this surprise you in either case?

## A For Loop and an Equivalent List Comprehension: Example 1

````python 
# a for loop
iterable = ['abc','def','hij']
container = []

for item in iterable:
    if len(item):
        container.append(item)
    
# an equivalent list comprehension

iterable = ['abc','def','hij']
container = [item for item in iterable if len(item)]



````

## A For Loop and an Equivalent List Comprehension: Example 2

````python
# for loop

squares = []
for num in range(10):
  squares.append(num**2)

print squares
````

````python
# list comprehension
squares = [num**2 for num in range(10)]
print squares
````


