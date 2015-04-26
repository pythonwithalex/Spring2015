## A Short Terminal Primer for UNIX-like Systems

#### What is a Terminal?

+ A terminal is a general term that stands for any text-only mode of interaction with an Operating System.
+ The essence of a terminal environment is the notion of the **READ EVALUATE PRINT LOOP (aka, REPL)** in which your typed commands are read and executed on a line-by-line basis.

````bash
al-laptop:data alexr$ date
Sun Apr 26 11:18:55 EDT 2015
al-laptop:data alexr$ whoami
alex
al-laptop:data alexr$

````

+ Terminals used to be the only thing between a user and a large multi-user mainframe.  Terminals as we use them in our class are really virtual terminals, in that they run inside a graphical environment on a workstation or personal computer.  
+ This means that the Apple Terminal is just the packaging for what we consider to really be the terminal, aka the REPL loop with the  `al-laptop:data alexr$` prompt.  
+ The Apple Terminal will by default give you a Bash shell. 
+ A shell is the interface between you and the Operating System.  You enter simple commands or lines of Bash programming code into the shell and these are in turn translated into commands by the Operating System's kernel and the actual bulk of the work is done.
+ To recap, Bash is 1) a shell that manipulates the Operating System and 2) the programming language that you use to manipulate the Operating System.   
+ When you login to a terminal, you see `al-laptop:data alexr$`.  This is a Bash prompt.

#### Filesystem Organization

An important part of using a shell is understanding how the system's files are organized. Mac OS X is more or less part of the Unix-like family of Operating Systems and thus its files are arranged in accordance with the Filesystem Hierarchy Standard.  In order to avoid boring you to death, just know that this means that the filesystem can be visualized as a tree.  The 'root' is considered the outer-most directory in that everything else is treated as if it's inside the root.  Inside the 'root' directory is a directory called /Users.  Inside /Users is the Student directory where we store our files. 

````
                          /
                 
   /Users               /Volumes                    /System   
     /Student             /Time Machine Backups       ....
       /Desktop
         lists.py
````

#### Terminal Prompt
`al-laptop:data alexr$`
The terminal prompt tells you a few things:
+ the name of your computer, `al-laptop`
+ the director you are in, `data`
+ your username

#### Recap
+ 'Terminal' is a general word to describe a interactive, text-based mode of computing.
+ 
