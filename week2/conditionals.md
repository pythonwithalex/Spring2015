While Loops run until the condition specified right after the 'while' becomes false. If that never happens, it runs forever!


````python
# WHILE
val = 9

while val > 0:
  print val
  val = val -1
````

In an if/else statement, the condition after the if is tested.  If that condition is True, the if block runs.  if it is False, the else block runs.
In a simple if/else, there is only one conditional and it comes after the if.  The else code runs only if the if conditional is false.
Note that in an if else, one of them ALWAYS executes.

Also, one and only one block of code is executed.  So, you can't have the IF and the Else blocks both run.  

Think of an if else as a cascade of separate 'Is this true?' questions.  If one doesn't run, the next one is checked. 
With that in mind, look at the following code.  The 'elif' only runs if the 'if' condition is false.

````python
# IF / ELSE  
if val == 10:
  print 'val is 10'

elif val == 7:
  print 'val is 7'

else:
  print 'oh, bother'
````

````python
# FOR LOOP
for num in range(val):
  print num
````
