## A Short Terminal Primer for UNIX-like Systems

#### What is a Terminal?

+ A terminal is a general term that stands for any text-only mode of interaction with an Operating System.
+ The essence of a terminal environment is the notion of the **READ EVALUATE PRINT LOOP (aka, REPL)** in which your typed commands are read and executed on a line-by-line basis.

````bash
student@computer ~$ date
Sun Apr 26 11:18:55 EDT 2015
student@computer ~$ whoami
alex
student@computer ~$

````

+ Terminals used to be the only thing between a user and a large multi-user mainframe.  Terminals as we use them in our class are really virtual terminals, in that they run inside a graphical environment on a workstation or personal computer.  
+ This means that the Apple Terminal is just the packaging for what we consider to really be the terminal, aka the REPL loop with the  `student@computer ~$` prompt.  
+ The Apple Terminal will by default give you a Bash shell. 
+ A shell is the interface between you and the Operating System.  You enter commands or lines of Bash programming code into the shell and it hands it off to a lower level where the actual work is done
+ To recap, Bash is 1) a shell that manipulates the Operating System and 2) the programming language that you use to manipulate the Operating System.   It works hand in hand with the lower levels of OS X that the user isn't able to access.
+ When you login to a terminal, you see `student@computer ~$`.  This is a Bash prompt.

#### Filesystem Organization

#### Terminal Prompt

The terminal prompt tells you a few things:
+ which directory you are in 

#### Recap
+ 'Terminal' is a general word to describe a interactive, text-based mode of computing.
+ 
