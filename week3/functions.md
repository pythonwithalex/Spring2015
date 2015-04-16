## Functions

In Math, functions take values in and map them to new values.
````
f(x) -> x*x
f(4) -> 16
````

This is a good starting point to understanding functions.  Think of a function as a black box that takes data in and sends data out.

````
4, 5, 6 --> FUNCTION --> 16, 25, 36
4, 5, 6 --> FUNCTION --> 15
````

In python, we must define our own functions before we can use them.  The functions we've been using (len, max, sum, etc...) have all been defined somewhere else before hand.  

We define a function like this:

````python
# this function takes arguments
def subtract(arg1,arg2):
  # code
  # code

# this function doesn't take arguments
def subtract():
  # code
  # code  
````

## Main points here:

+ A function definition is needed to create your own function.
+ A function needs to be defined before you call it in your code.
+ A function definition starts with `def <function_name>(<comma-separated list of names for input values>)`
+ 'names for input values' are technically called **parameters**
+ arg1, arg, ... etc are all optional but if you want your function to transform data, you probably want to use parameters in your function. Separate each parameter with a comma.
+ After the `def` statement line, indent 4 spaces before entering your code. Indent 4 more spaces for any containing `for` or `while` loop.

## What is the Point of a Functions?

Here's a Trivial Example, that doesn't really express the point:

````python
# function definition
def sample_func(a,b):
  print a,b

# now that it's defined, I can use it
sample_func('alex','ramsdell')
# prints 'alex ramsdell'
````

Given the above example, you might ask, 'Why do I need a function to simply print two values?'.  That's a reasonable question, so here is a less trivial example.   

````python
def makePerson(first_name,age,height_string):
  person = []
  person.append(first_name,age,height_string)
  return person
  
people = []
names = ['make','bobby','zan','beatrice','markus']

for first_name in names:
  age = random.randrange(4,100)
  feet = random.randrange(4,8)
  inches = random.randrange(0,11) 
  height_string = '{}ft, {}in'.format(feet,inches)
  # And here we call the makePerson function.
  people.append(makePerson(first_name,age,height_string))

for person in people:
  print person
````

#### Question:

We didn't need the function makePerson to make Mike.  Why did we use the function? I can think of at least three reasons why a function is useful.

#### Your Challenge:

Write a program that doubles the square of a third of the reverse of the max of this list: [01,94,30,3.0,53]. It should have five functions that do the work of accepting arguments and calling them, plus a main function that 'wraps' the program.

Please try any approach you like, just don't do this: 

````python
def main():

    return func5(func4(func3(func2(func1()))))

main()
````
