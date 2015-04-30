#### Dictionaries

note: see my [slides](https://docs.google.com/presentation/d/1K2zssbmjiyTwdSCUajrJADRrKvELNCGsfcs2ak8EDu8/edit?usp=sharing) for more on dictionaries.
A dictionary is a data structure that holds {key, value} pairs. Other languages refer to this class of data structure as an *associative array* or a *hash map*.

We say that a Python dictionary 'maps' keys to values. In other words, you perform a *dictionary lookup* like this:

````python
ball['weight']
````
and get a value back:
````python
15.2
````
In this example, the *key* is `weight` and the *value* is `15.2`.

Let's backup for a second.  How do we create a dictionary object? Well, there are two ways:

````python
# the explicit way, using a dict() 'construtor' function:
ball = dict()

# a dictionary literal
ball = {}
`````
You can use either of these methods, but note the syntactic differences in the 'Alternate Methods' section below for each method.

Once you've created a dict object, you can add values to it like this:

````python

ball['weight'] = 15.2
ball['pos'] = [3,4]

````

#### Alternate methods of creating a dict()
````python
# create a dict and populate it with values all at once
d = dict(a=1,b=2,c=3)
print d
{'a': 1, 'b': 2, 'c': 3}

# an equivalent method using the literal syntax
d = { 'a' : 1, 'b' : 2, 'c' : 3}

# the same as above, but formatted nicely
d = {
     'a' : 1,
     'b' : 2,
     'c' : 3
    }
````

Note that with `dict(a=1,b=2,c=3)`, the keys are not explicitly strings when we pass them in, but they are converted to strings by the `dict()` constructor function.  

Declaring a dictionary with the literal syntax (i.e., using `{}`) affords you more flexibility.

````python
import math

d = {
      'a' : 1,
      (1,2) : 2,
      math.sqrt(9): 3
    }
print d
{3.0: 3, 'a': 1, (1, 2): 2}

````

#### Some Facts about Dictionaries

+ They are incredibly useful for storing data under human-friendly labels known as **keys**. 
+ Dictionaries may *seem* to store their keys and values in an dependable order, but they in fact do not.  Try writing a python script that creates a dict and prints out the values.  Run it.  Then reboot your computer and run it again.  You will find that the results differ.  Key point: do not use them as a container for sequential data.
+ Dictionary keys must be immutable, meaning you can't use a list as a key that maps to some value. You can use a tuple (which we haven't really covered) because a tuple is an immutable type.

````python
l = [1,2]
mydict[l] = 
TypeError: unhashable type: 'list'
l = (1,2)
mydict[l] = '0x55aa'
print mydict[l]
0x55aa
````

#### The Importance of Dictionaries


The inner workings of dictionaries are somewhat complex but they reflect a concerted effort to make lookups very fast. 

They also take a lot of the mental load off the programmer. 

If you recall, with a list you need to remember the position that something is in. 

Imagine breaking a text file up into sentences and then words in order to do some processing to it. 

It is doable with lists, but it may make you think much more than necessary because you will have to remember which numbers correspond to which objects you've created by splitting the text up. 

With dictionaries, you can assign these objects meaningful names like textFile['lines'] = [l for l in f.split('.')]. You can use things with meaning to you to identify the location of important data. 

#### Further Reading

+ [The Mighty Dictionary](https://www.youtube.com/watch?v=C4Kc8xzcA68)
+ [Loop Like a Native](https://www.youtube.com/watch?v=EnSu9hHGq5o)
