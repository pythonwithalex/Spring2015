## Fizz Buzz

## Reading a File

You can open a text file and store the contents as a string like this:

````python

f = open('textfile.txt','r') # file should exist in same dir where you're calling your script
content = f.read()
print type(lines)
# prints str
````
You can open a file and store it as a list of lines this way:

````python

f = open('textfile.txt','r')
lines = f.readlines()
print type(lines)
# prints list
````

## 
