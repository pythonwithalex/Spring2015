# For Loop

Python `for` loops iterate through an object and give you the value at each index.  

`Note to folks who program in C, C++, C#, PHP, JavaScript and some others: Python gives you the value, not the index.`

For loops always start with: `for <item copy> in <list object>:`

the `list object` is a list you created prior to for loop.  `item copy` is created at the time we enter the for loop and you should think of it as the current item in the loop.

`item copy` is a copy of the item in the `list object`, not the actual item. It makes some sense: often you want to gather a subset of values from a larger range.  create a list and append to the list the values 



# The While Loop
While Loops run until the condition specified right after the 'while' becomes false. If that never happens, it runs forever!


````python

# set a start value
start = 9

# decrease it by one each time
while start > 0:
  print start
  start = start -1

# this one never stops

start = 9
while val > 0:
  print val


````

# The If / Else

````python
if <condition>:
    indented code
else:
    indented code
````

+ In an if/else statement, statements are checked in the natural reading order.  
+ Whever there is an `if` or `elif`, there is a condition being tested.  
+ If that condition being tested evaluates to True, the block's code runs.  
+ After an `if` statement runs, python looks for more `if`s, and if they exist, it runs them. if they don't, it exits the `if else` block.
+ `if`s are not mutually exclusive, meaning you can run multiple `ifs`
+ `elif` and `else` are mutually exclusive. After one of these runs, we exit the `if else` block.

You can check for some condition and act accordingly with just a single if:


````python
it_is_raining = True

if it_is_raining:
  load(umbrella, boots)
  
````


If you want to check for a bunch of things and in each case do something, you can use multiple ifs:

````python

if it_is_raining:
  load(boots,umbrella)

if it_is_cloudy:
  load(backpack,walking_stick)
  
elif it_is_sunny:
  load(sunglasses,hat)
````

You can use `elif` if you have code you want to run if True and then exits. 

````python

it_is_sunny = False
it_is_raining = True

if it_is_raining:
  load(umbrella,boots)
  
elif it_is_sunny:         <- if it's sunny, load sunglasses and hat and then exit the block
  load(sunglasses,hat)

else:
  print 'what is like outside?'
````

