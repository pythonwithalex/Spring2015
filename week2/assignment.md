## 1) Fizz Buzz

" Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”. " 

## 2) CSV Format

Your assignment is to write code that opens a CSV file on your computer, reads it in, processes it, and prints it out in a way that's nice to read. You should try to justify the text consistently like the following output:

````python

firstName  |  lastName  |  age  |  profession

Michael       Jordan       52      Basketball Player
Kirsten       Bell         39      Actress
Morrissey                  60      Musician       

````

The structure of our data is like a spread sheet.  here are the file column names: 

firstName, lastName, age, profession

and here is some sample data:

+ 'Michael', 'Jordan', 52, Basketball Player
+ 'Kirsten','Bell', 39, Actress
+ 'Morrissey',, 60, Musician

#### How to Open a File and Read Data

You can open a text file and store the contents as a string like this:

````python

f = open('textfile.txt','r') # file should exist in same dir where you're calling your script
content = f.read()
print type(content)
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
