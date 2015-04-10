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
    indented code
````

In an if/else statement, statements are checked in the natural reading order.  Whever there is an `if`, there is a condition being tested.  If that condition is True, the `if` block runs.  If it is False, the `else` block runs.

You can have an if with no else:

````python
it_is_raining = True

if it_is_raining:
  load(umbrella)
  
````

You can have multiple `if`s:

````python

it_is_sunny = False
it_is_raining = True

if it_is_raining:
  load([umbrella,boots])
  
if it_is_sunny:
  load([sunglasses,hat])

else:
  load()
````

... and there is an `elif` , which is short for `else if`

````python

it_is_sunny = False
it_is_raining = True

if it_is_raining:
  load([umbrella,boots])
  
elif it_is_sunny:
  load([sunglasses,hat])

else:
  sys.exit(1)
````

Note that in an if/else, one and only one block code ALWAYS executes. That's because it is either raining or it isn't raining.  That is the nature of logic. It can't be both raining and not raining.

Think of an if else as a cascade of separate 'Is this true?' questions that stops once one of them is true.  If one doesn't run, the next one is checked. If it gets to the 'else', it will just run.

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
