# For Loops

This is what a `for` loop looks like:

```python
grocery_list = ['bread','eggs','cheese','corn','cereal']
for item in grocery_list:
  purchase(item)
````


it would print the following: 
````python
'bread'
'eggs'
'cheese'
'corn'
'cereal'
````

Python `for` loops iterate through an object and give you the value at each index.  You can put that value in a list if you want, or call a function with that value as input.  

`Note to folks who program in C, C++, C#, PHP, JavaScript and some others: Python gives you the value of item in the example above, not the index of that value.`

For loops always start with: `for <item copy> in <list object>:`

The `list object` is a list you created prior to the `for loop`.

`item copy` is created at the time we enter the for loop and you should think of it as a name bound to the current item in the `list object`.

Here's an example:
```python

results = []
values = [1,2,3,4,5,6,7,8,9,10]

for value in values:
  if value > 4:
    results.append(value)

print results
# [5,6,7,8,9,10]
````

One important thing I should note is that `item copy` is a copy of the item in the `list object`, not the actual item. There is a nice way to modify the actual object, but that is for later. The fact that `item copy` is a copy makes some sense: often you want to gather a subset of values from a larger range.  Create a list, iterate through it with a `for item in yourlist` and use the `if / else` statements (explained below) to conditionally add values to a `results` list.

# While Loops

While Loops run until the condition tested  after the 'while' is false. If the first test is False, it never runs at all. If the condition is never false, it runs forever!

An example of the application of an 'infinite' while loop might be a webserver application (the one below is conceptual):

````python
def serve_the_web():
  while True:
  
    request = getHTTP_Request()
    sendHTTP_Response(response)
    if critical_error:
      break
```

Another would be a counter:

````python
# set a start value
start = 9

# decrease it by one each time
while start > 0:
  print start
  start = start -1

# this one never stops

start = 9
while start > 0:
  print start
````



# If, elif and else statements

````python
if <condition>:
    indented code
else:
    indented code
````

+ In an if/else statement, statements are checked in the same way you would read them, top to bottom 
+ Whever there is an `if` or `elif`, there is a condition being tested.  
+ If that condition being tested evaluates to True, the block's code runs.  
+ After an `if` statement runs, python looks for more `if`s, and if they exist, it runs them. if they don't, it exits the block.
+ `ifs` are mutually exclusive from `elifs` and `elses`, they never both run
+ `if`s are not mutually exclusive with themselves, meaning you can run multiple `ifs`
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

