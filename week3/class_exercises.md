## Loop 'equivalence'

#### While loop

````python

n = 0
while n < 5:
  print n
  n = n + 1
````

#### For loop


````python

for n in range(5):
  print n

````

#### Questions:
+ In the while loop, why would it be a bad idea to print `n` on the last line of the loop?
+ What is the value of `n` after the for loop completes? after the while loop completes? Does this surprise you in either case?

## For Loop and List Comprehensions

````python

squares = [num**2 for num in range(10)]
print squares
````

````python

squares = []
for num in range(10):
  squares.append(num**2)

print squares
````
