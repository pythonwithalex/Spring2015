## Week 2 Recap

#### Accessing Values in Strings and Lists

##### Iterables

Any data type that you can validly use in a `for` loop in Python is called an **iterable**.  An iterable simply means you can access the values in it one at a time.

Iterables support a uniform method of access. We can access their constituent parts using brackets if we put a numerical position inside it. 

Here's an example (I'll use 'e' and 'names' for all the examples here):

````python
>>> e = 'elephant'
>>> print e[0]
'e'
>>> names = ['jean', 'mike', 'joe']
>>> print names[1]
'mike'
````

We can also read subsections from each with the same syntax:

````python
>>> print e
'elephant'
>>> e[:2]
>>> 'el'
>>> print names
['jean', 'mike', 'joe']
>>> names[:2]
>>> ['jean' , 'mike']
````

Note the following:

+ we are reading data here from each object, not writing data to it
+ the syntax we use is uniform across two distinctly separate types of data
+ this syntax uniformity is a feature
+ being able to get the last character or last item with [-1] makes our code easier to write and easier for ourselves and others to understand 

What about *writing* data to strings and lists?

Let's try it:

````python

>>> print names
['jean', 'mike', 'joe']
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

+ strings don't provide a way to assign data to their individual parts. 
+ strings are 'read only'. 

There are two computer science terms that you should be familiar with that describe whether a data type is read-only or not:

#### mutability

+ a mutable object can grow, shrink or change and it's still considered the 'same' object
+ every distinct object in python has a unique identifier, which you can find with the built-in function `id()`
+ `id(names)` will give you a large integer that corresponds to the location of the object
+ when we append a new name to `names`, `id(names)` will still return the same large integer

#### immutability

+ once the object is created, any changes to it are all-or-nothing (and they're not strictly changes *to* the object because the only sort of change you can make is the creation of a new object under the same name, but it will be a separate, independent string).  
+ Thus, you can't assign new values to subsections of it with `e[0] = 'x'`
+ if you want to change what your name refers to, you have to reassign a value to the object's name

````python
lang = 'python'
lang = 'python2.7'
````

## Why does all of this matter? 

String and list methods are productive features of the python language.  But they will be frustrating for you if you don't have some familiarity with the idea of mutability and immutability and the knowledge of which Python data types fall under these two categories.

## What is a method?

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

So, to recap: if you see '( )', that's a function call.  if the function has a dot preceding it, it's a method.  Otherwise, it's a regular function.


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
But back to the burning question ...

## What does mutability / immutability mean for my code?

If you understand the distinction, you will have less to debug and thus more fun per line of code.

We can break all methods down into roughly two types: 

+ methods that give you back a useful, totally independent value ( all string methods, list methods that read a value )
+ methods that modify themselves and don't pass back a useful value (list methods that change the list such as .sort()) reverse(), etc)


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
Why did the sorted_names have the value 'None' ?

+ Remember, the .sort() method doesn't output any data, it changes the values of the object on which it was called, names
+ a method, like any function,  isn't required to explicitly pass a value back to the program.
+ But it always passes something back, and if nothing is explicitly passed back, it defaults to passing None back.
+ so we assigned the default value None to the name `sorted_names`

to summarize: 
+ `names.sort()` is a function that actually writes new values to `names`.  
+ `names.index()` just reads information from `names`, so nothing actually changes.

## Using the string `.split()` method

We can turn `'jean wendy joe'` into `['jean', 'wendy', 'joe']` by running this code:

````python
people = 'jean wendy joe'.split()
````

You can do useful things like checking a paragraph for properly capitalized sentences.

````python

#open the file, 'r' for read-only
paragraph = open('paragraph.txt','r')

# read the file into a string
content = paragraph.read()

# split string into words 
words = content.split()

# for each word, if prior word has a '.' at the end, 
# capitalize this word and assign it to this index in the original words array
for index, word in enumerate(words):
  if (index - 1) and words[index - 1].endswith('.'):
    words[index] = words[index].capitalize() 

````


#### Copying Lists

What do you expect a, b and c to be after the lines below?

````python

a = [1,2,3]
b = [4,5,6]
c = a
a[0] = 3
c[0] = 1

````
a,b,c look like this

````python

print a,'\n', b, '\n', c
[1,2,3]
[4,5,6]
[1,2,3]

````

the annotated version of the code above:

````python

a = [1,2,3]
b = [4,5,6]
c = a       # c is an alias for a, so c[0] is really a[0]
a[0] = 3    # a is [3,2,3]
c[0] = 1    # a is back to the old [1,2,3]

````

When you assign a list object to a name with `c = a`, a new object c is **not** created.  Instead, the new name c becomes another way to refer to the value to which a refers.

a -> list_obj
c -> list_obj

If you want to copy a list's values into another list so that you can edit one and the other will not be affected, use this method:

````python

a = [1,2,3]
b = [4,5,6]
c = a[:]
a[0] = 100
print a, '\n', c
````

This is a convenient syntax to copy all of the items in a list. No for loop needed.

#### EXTRA INFO:

if you know the number of items in a list, you can name each assign a name to each item by separating the names by commas:

````python
a=[1,2,3]
one, two, three = a[:]
print a
print one,two,three
````

````


````
