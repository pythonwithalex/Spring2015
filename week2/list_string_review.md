## Week 2 Recap

#### Accessing Values in Strings and Lists

Both strings and lists are indexible in the same way, meaning that we can access their constituent parts  using the bracket [] syntax and a numerical position inside it. 

Here's an example (I'll use 'e' and 'names' for all the examples here):

````python
>>> e = 'elephant'
>>> e[0] is 'e'

>>> names = ['jean', 'mike', 'joe']
>>> print names[1]
>>> 'mike'
````

We can also read subsections from each with the same syntax:

````python
>>> e[ : 2]
>>> 'el'
>>> names[:2]
>>> ['jean' , 'mike']
````

Note the following:

+ we are reading data here from each object, not writing data to it
+ the syntax we use is uniform across two distinctly separate types of data
+ this syntax uniformity is a feature
+ being able to get the last character or last item with [-1] makes our code easier to write and easier for ourselves and others to understand 

What about writing data to Strings and Lists?

Let's try it:

````python

>>> names[1] = 'wendy'
>>> print names
>>> ['jean', 'wendy', 'joe']
````

That was successful.  'Mike' became 'Wendy'.

Now I'll try with the string 'elephant'

````python

>>> e[0] = 'a'
TypeError: 'str' object does not support item assignment
````

In English, the error message is telling us:

+ that strings do not provide you with the ability to assign data to its individual parts.
+ strings are 'read only'. 

There are two computer science terms that you should be familiar with that describe whether a data type is read-only or not:

mutable
+ the object can change and it's still considered the 'same' object
+ every object in python has a unique identifier, which you can find with the built-in function id()
+ id(names) will give you a large integer that corresponds to the location of the object
+ when we append a new name to names, id(names) will still return the same large integer

immutable
+ once the object is created, any changes to it are all-or-nothing (and they're not strictly changes).  
+ Thus, you can't assign new values to subsections of it with e[0] = 'x'
+ if you want to change what your name refers to, you have to reassign a value to the object's name
lang = 'python'
lang = 'python2.7'


Why does all of this matter? 

String and list methods will be confusing without some familiarity with the idea of mutability and immutability.


What is a method?

A method is a function that is a part of an object such as a list or a string.  You'll know when a method is used because you always see a dot followed by a function call.

An example with the string.upper() method:

````python

>>> e
>>> 'elephant'
>>> e.upper()
>>> 'ELEPHANT'
>>> e.upper
>>> <function upper>
````

In the last two lines, we see what happens when we try to call a function 'incorrectly', meaning that we forgot the parentheses.  A this point, if you see this in the output of your code, you most likely forgot the parentheses.

So, to recap: if you see '()', that's a function call.  if the function has a dot preceding it, it's a method.  Otherwise, it's a regular function.


sum is a regular function

````python

>>> sum([1,2,3])
>>> 6
````

e.upper() is a method
````python
>>> e.upper()
>>> 'ELEPHANT'
````
But back to the burning question:  What does mutability / immutability mean for my code?

Well, there are two types of conventional methods: 

1) the type that gives you back a new, totally independent value      [ all string methods and list methods that read a value ]
2) the type that modifies 'itself' and doesn't give you back any value       [ list methods that change the list, like sort, reverse, etc]


Typically, string methods operate like type #1 because you can't change them, so you get a new, independent value back that you can store under a different or even the very same name
````python

>>> print e
>>> 'elephant'
>>> big_e = e.upper()
>>> big_e
>>> 'ELEPHANT'
````
Here, I assigned the value of e.upper() to a new name, big_e.
````python

>>> e = e.upper()
>>> print e
>>> 'ELEPHANT'
>>> print e.lower()
>>>  'elephant'
>>> print e
>>> 'ELEPHANT'
````
Here, I overwrote the original e with the value of e.upper().  Then I merely printed our new value of e as lower case by using the .lower() method.  But as you can see in the last line, this didn't change e.  e is still in caps.

List methods generally modify the list if they are 'write' operations, such as names.sort(), names.insert() or names.reverse()
They don't modify the list if they are 'read' operations, such as names.index('wendy'). 

````python
>>> print names
>>> names is ['jean', 'wendy', 'joe']
>>> names.sort()
>>>
````

notice names.sort() didn't output any value

````python
>>> print names
>>> ['jean', 'joe', 'wendy']
````
but names.sort() did in fact sort the list

````python
>>> sorted_names = names.sort()
>>> print sorted_names
>>> None
````
Why did the last three lines result in the output 'None' ?

+ Remember, the .sort() method doesn't output any data, it changes the values of the object on which it was called, names
+ a method, like any function,  isn't required to explicitly pass a value back to the program.
+ But it always passes something back, and if nothing is explicitly passed back, it defaults to passing None back.

to summarize: names.sort() is a function that actually writes new values to names.  
names.index() just reads information from names, so nothing actually changes.

Using the string .split() method

We can turn 'jean wendy joe' into ['jean', 'wendy', 'joe'] by running this code
people = 'jean wendy joe'.split()

You can do useful things like checking a paragraph for properly capitalized sentences.

````python

#open the file, 'r' for read-only
content = open('paragraph.txt','r')

# read the file
content.read()

# words 
words = content.split()
for index, word in enumerate(words):
  if (index - 1) and words[index - 1].endswith('.'):
    words[index] = words[index].capitalize() 
  
````

Why did we turn a string into a list yesterday at the end of the exercise?
