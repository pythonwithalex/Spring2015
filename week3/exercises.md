## Programming With Python 
# Week 3 Exercises 

#### A note before you start: Programming is problem solving.  Start simple and build up.  Break a problem into smaller parts. 

## Short Exercises 

+ write a function that prints "hello,world" 
+ write a function that takes in a name and prints "hello, <name>" 
+ write a function that prints the square of 12 
+ write a function that takes a number as input and prints that number squared 
+ write a function that prints the sum of the squares of 1 to 10 (including 10) 
+ write a function that prints the sum of the squares of NUM to a higher NUM (including higher num) 
+ write a function that takes a number as input and prints the number of digits it has 
+ write a function that removes last letter of a string 
+ write a function that tells us if a string contains a certain letter 
+ write a function that splits a sentence into words and sorts by word a-z 

HINT FOR THE LAST TWO SHORT EXAMPLES: 
the % (modulo) operator will tell you the remainder when you divide a number by another number. 
examples: 
in general: a % b means 'what is the remainder when you divide 'a by b' ? 
24%12 = 0 
10%3 = 1 
3%10 = 3 (why, you ask? how many times does 10 go into three? And what's the remainder?) 

write a function that prints the multiples of 5 under 200. 
write a function that prints the multiples of 3 AND 5 under 200. 




MORE COMPLEX PROBLEMS 

1) Word Count 

Write a function that prints out each letter in elephant and the number of times it occurs in the word. 
Ideally, you don't want to print out duplicate letters and their counts twice. 
If you can do that, print them out in alphabetical order. 

hints: 

Look at string methods (functions attached to strings) in iPython by typing a dot after your string, then hitting tab. It should display what functions and data is available to you. 

Using a dictionary for this one will be helpful 



2) Internet Time 

This is how you import the datetime module into a python file: 

from datetime import datetime 

this is how you get the current time: 

print datetime.now() 

You'll notice that what it prints is not exactly immediately useful to the ordinary person. It needs to be manipulated. Convert datetime.now() to a string and use the .split() method to save as variables only the parts you want to keep. Give the variables reasonable names: hours, minutes, month, etc. 

Then write a program that prints out the following sentence, filling in the variables: 

"Hello, it is now <Hour>:<Minute> on <Weekday>, <Month> <Day of the Month>." 

3) Font Proportions 

I have a list of fonts-sizes that designer David Kadavy says I should remember and use: 

5 
7 
9 
16 
21 
28 
37 
50 
67 
83 

I believe that the scale may be useful, but I'm not so sure I believe that font size '8' is off limits. Write a function that will give me a 'proportional' set of numbers if I decide to use 6 or 8 or 9, etc ... as my lowest font size. 

5 -> 8 
7 -> ? 
9 -> ? 
16 -> ? 
21 -> ? 
28 -> ? 
37 -> ? 
50 -> ? 
67 -> ? 
83 -> ? 



4) Flask Time 

Part 1: 

Go to http://flask.pocoo.org and copy the 'Flask is Fun' section into a file called run.py, save it, and run it in your Mac Terminal. 

If it works, it will say: 

* Running on http://127.0.0.1:5000/ and some other stuff. 

Put that http address into your web browser and go there to verify it's working. 

Part 2: 

Get the hello() function to return the square of some number. 

Part 3: 

Let's use Flask for something a little more useful. If you haven't done MORE COMPLEX PROBLEMS #2, which asks you to use the datetime module to get the current time, do that now. Then, put the contents of that into your run.py's hello() function. Change 'def hello():' to 'def flaskTime():' Then stop the flask server and start it again. 


5) Cipher - Don't attempt this unless you're able to do the other Complex Problems 

type 'import this' into iPython and read the output. 
then type 'print this.s' 
write a function to convert this.s into the output of 'import this' 

hints: 
ord('a') gives you a numeric representation of a 
chr(97) turns 97 into its alphabetic representation, 'a'. 
http://www.rot13.com/info.php 
modulo (%) is a useful operator when keeping values in a specific range 
