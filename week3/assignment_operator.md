THE ASSIGNMENT OPERATOR 

First, ask yourself: what is happening when we use '=' ? 

Usually, when we declare a variable name for a list or a string, we do this: 

l = [1,2,3,4] 
or 
s = ['a','b','c','d'] 


You can think of this as the expression of a general form we use in assignment: 

name refers to value 
or 
name gets value 


We give a value a name so we can refer to it and change it if needed during the run-time of our program 

You may think this is obvious, but because we often learned a meaning for '=' way before we started programming, we can sometimes let the mathematical sense of '=' creep into our programming logic. 

here's an algebraic equation that expresses the length of the two sides and hypotenuse of a right triangle: 
c**2 = a**2 + b**2 

The way to find the value of c in Python: 

import math 
a=5 
b=6 
c = math.sqrt(a**2 + b**2) 
print c 
7.810249675906654 

if you try doing it this way: 

math.sqrt(c) = a**2 + b**2 

or this way 

c**2 = a**2 + b**2 

you get the errors: 

'SyntaxError: can't assign to function call' and 'SyntaxError: can't assign to operator', accordingly 

This is because the left hand side must be the name to which you want to assign a value. 
c**2 is not a name, it is an expression that implies you want the computer to fetch the value of c and compute the result of c multiplied by itself. Thus, it belongs on the right hand side. 


So, '=' doesn't mean equivalence at all. In fact, '==' is a way to test for equivalence, and this doesn't set two things to be equivalent in the sense of establishing this truth. '==' instead compares two objects to see if they're values are equivalent. It says, "I'm going to test whether the things on either side of me are equal and return True if so and False if not." And it returns either True or False. 

So, the name 'l' for the list [1,2,3,4] is not equivalent to the list. 

What is it, then? 

Simply put, its an address. For the programmer, 'l' is a human-readable way to store and locate a list's values. The computer converts it into a number that corresponds to an address where the variable is located in memory. 

A value can go without a name, but a name can't go without a value. 

If you write a script with just the letter 4 in it, and run it ('python four.py'), it will run and you won't see any output. That's because the computer says, "Evaluate 4. OK, done." 

But if you write a script with the following in it: 

myList 
print myList 
In Python, those will give you 'NameError: name 'myList' is not defined' errors because you are asking where to find something that doesn't exist. 


What about this: 

l[0] = 10 

is l[0] a name? 

It is. It says, find the location of 'l' and give me the value at 0 offsets from there. 

