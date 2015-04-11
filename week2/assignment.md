## Assignment for week 2

Please do as many of these as you can.  If you have trouble, you can email me or bring specific questions to class.

## 1) Sum all the numbers containing a '9' between 0-50 and 100-150, non-inclusive (meaning, the upper bound of each range is not included).

## 2) Fizz Buzz

" Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”. " 

## 3) CSV Format

CSV is a file structure where a single record consists of values separated by commas and ends with a newline.  The first line is the Column headers.

```csv
average, mean, mode # column headers

8.4, 9.0, 8.0 # an individual row
2.3, 3.0, 3.4
90, 92, 90 
45, 60, 55
````

Your assignment is to write code that opens a CSV file on your computer, reads it in, processes it, and prints it out in a way that's nice to read. Assume that no record (aka, row) ever exceeds four columns, but that it can have missing fields.  I've shown you below how to open a file in python.

requirements: 

+ You should try to justify the text consistently like the sample output below
+ Also, try to be as fault-tolerant as possible.  If a field is missing, do you handle that? What if age data ends up in the profession column?

````python

sample printcsv.py output

firstName  |  lastName  |  age  |  profession

Michael       Jordan       52      Basketball Player
Kirsten       Bell         39      Actress
Morrissey                  60      Musician       

````

The structure of our data is like a spread sheet.  Here are the file column names: 

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
f.close()
print type(content)
print content

````

You can open a file and store it as a list of lines this way:

````python

f = open('textfile.txt','r')
lines = f.readlines()
f.close()
print type(lines)
print lines
````

