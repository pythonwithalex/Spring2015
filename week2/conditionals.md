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

In an if/else statement, the condition after the if is tested.  If that condition is True, the if block runs.  if it is False, the else block runs.
In a simple if/else, there is only one conditional and it comes after the if.  The else code runs only if the if conditional is false.

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
