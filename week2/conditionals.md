# For Loop

for loops have the structure

````python
for <item copy> in <list object>:
  # code 
````

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

You can check for some condition and act accordingly with just a single if:


````python
it_is_raining = True

if it_is_raining:
  load(umbrella, boots)
  
````


You can use `elif` to check for alternate conditions but then exit the if / else block when the `elif` condition is True. 

````python

it_is_sunny = False
it_is_raining = True

if it_is_raining:
  load(umbrella,boots)
  
elif it_is_sunny:
  load(sunglasses,hat)

else:
  sys.exit(1)
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

With that in mind, look at the following code.  The 'elif' only runs if the 'if' condition is false.

````python
# IF / ELSE  

it_is_raining = True

if it_is_raining:
  print 'why, Boston, why?'

else:
  print 'oh...great!'
````

````python
# FOR LOOP
for num in range(val):
  print num
````

