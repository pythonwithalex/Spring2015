## Week 1 Review

#### A Note on Questions

Please ask questions! Everyone benefits from questions so please don't be shy.  

#### Our Tools

Apple Terminal - this will be our programming environment for this course.  This means that we will run everything (except our Text Editor) from the terminal. Instead of manipulating the Operating System via a mouse, you are giving the operating system instructions in the form of text.  Part of learning to program in any language is learning more about your computer: how it works, the various tools that it offers you, efficient workflows, programmatic thinking.  A Graphical environment simplifies things, but it can also hide ways to do things more efficiently and with greater control.

You can start the Terminal from /Applications/Utilities/Terminal, or with the shortcut sequence:  ⌘ + Spacebar + 'Terminal'.

Any terminal generally has two states: 
+ It waits for you to enter input
+ It runs your commands.  

The line of text that appears when it is waiting for you to enter a command is called a prompt. It tells you which user you are and which directory you are in the filesystem ('~' means /Users/Student in our case). You enter a command by typing it into the terminal and then hitting return. If you have requested information back, it will display it and then show you a new prompt.  If a command isn't supposed to print any information, then you will just see a new prompt.

Here's an example:

````bash
alex@terminal $ whoami
alex
alex@terminal $

alex@terminal $ mv file1.txt file2.txt
alex@terminal $
````

IPython - from the Apple Terminal, type 'ipython' and press Enter, like this:

````bash
alex@terminal $ ipython
In [1]: print 15
15
In [2]: print 15*30
450
In [3]: print 'abc'
abc
````

The IPython application is a terminal interface between the python interpreter and you, the programmer.  Whereas the Apple Terminal lets you manipulate the OS in a pretty direct way ( you can find out which directory you are in, transfer files, edit files, etc all from the terminal), the IPython interpreter allows you to enter python statements and python interpreter specific commands.

#### What is a Program? 

A program is a set of statements that ask a computer to do specific things. A program is useful if it completes a specific task.  A task could be very simple, or it could could be comprised of multiple separate tasks that handle distinct sub-parts of the original task.

Examples of simple tasks that we might want a computer to do for us:

1. Find the perfect squares below 200

In Python:
````python
import math
max = 200
perfect_squares = [ num for num in range(1,max) if math.sqrt(num) %2.00 == 0 ]
print perfect_squares
````

2. Open a file and read it line by line, printing only the lines that contain a specific word.

In Python:
````python
f = open('myparagraph.txt')
content = f.readlines()
f.close()
for line in f:
  if 'scientific' in line:
    print line
````

You usually type these statements into a text editor, save it as a .py file, and then run the file from the terminal.  The python program you run from the terminal reads in your source file starting at the top of the file until it reaches the bottom, attempting to translate the statements into code that the machine can then run. When the code is fully translated (and the syntax is error-free), it runs your program.  When the program runs, if you have asked the computer to print information in your program, you will get some output in the terminal.  Otherwise you won't get anything.  Or you'll get error messages from Python.  The code I've given above may look complicated at this point (soon, it won't be, I promise), but the language that it gets translated into is much more complicated as it doesn't contain anything that a human could easily remember.  Fortunately, we don't worry about the translation, just the python code.  


Running the Code Example:

Let's say the 2nd example I gave you above is a program saved in a file called showlines.py.  I would run this like so:

````bash
alex@terminal $ python showlines.py
Your explanation isn't very scientific, but it does make sense to me.
Most scientists would agree that scientific inquiry is at the heart of progress.
alex@terminal $
````

In the example above, we told the Python interpreter to execute the python file showlines.py.   
The interpreter reads the python program and attempts to make sense of the code there.
If the program has no syntax errors, the statements are then executed

#### Parts of a Program

**Comments**: Any line with # at the beginning is a comment.  This means that the python interpreter 'knows' ahead of time to ignore those lines.

**Variables**: A variable is a name for a continually available place in storage where you want to put a certain value.  You call it something that is easy to remember and descriptive so that you can refer to that value again at any time.  

name = 'Robert'
new = False
count = 15

**Operators**: These operate on/ perform computations with values. Some are binary (require two values) and some are not. We will mostly use binary operators.

**Expressions**: An expression is a set of one or more values that are 'operated' on. operators reduce a number of values to less values, usually one, so that the computer can use the computed value.

5
4*4
Math.sqrt(4)
4 - 0

**Statements**:  A statement results in a change in the program's overall data.  One sure sign that you're looking at a statement is that it includes a single equals sign, '='.  This is a sure sign because the '=' means "keep track of this value by this name".  But statements aren't limited to explicit assignments.  They can be things like import statements or even just literals.

**Variable Assignment**: an assignment is a statement that uses a variable name, the '=' operator, and an expression.   The rule is that the left hand side of '=' is always the name for a value stored in memory and not a useful value itself.


#### Why Variables?

They save you repetition and lend some humanity to your program.

Look at a few cases with variables:

Some variables are replaced with new values rapidly

````python
for item in my_grocery_list:
  print item
````

some variables don't change at all

````python
GRAVITY = 9.8
PI = 3.14
````

and some change at random 
````python
tomorrows_weather = weather_miner.tomorrow['description']['short']
````
