## A Short Terminal Primer for UNIX-like Systems

#### What is a Terminal?

+ A terminal is a general term that stands for any text-only mode of interaction with an Operating System.
+ The essence of a terminal environment is the notion of the **READ EVALUATE PRINT LOOP (aka, REPL)** in which your typed commands are read and executed on a line-by-line basis, while you supply commands to be executed.

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

An important part of using a shell is understanding how the system's files are organized. Mac OS X is more or less part of the Unix-like family of Operating Systems and thus its files are arranged in accordance with the Filesystem Hierarchy Standard.  In order to avoid boring you to death, just know that this means that the filesystem follows a standard that makes it easy to locate common and essential files.  Also, this means that the Mac OS X filesystem can be visualized as a single tree.  The 'root' is considered the outer-most directory in that everything else is treated as if it's inside the root.  Inside the 'root' directory is a directory called /Users.  Inside /Users is the Student directory where we store our files. 

````
                          /
                 
   /Users               /Volumes                    /System   
     /Student             /Time Machine Backups       ....
       /Desktop
         lists.py
````

**Note**: On a Windows machine, you will have a C drive and maybe a D drive if you have a separate data partition, and if you mount an external drive, that will have be organized under a new, separate drive letter, maybe Z.  Unix-like filesystems don't do this.  This is not in accordance with the Filesystem Hierarchy Standard because the entire computer is not organized as a single tree.  In contrast, in OS X, we have the '/' or root directory as the very top-level of the filesystem.  If we mount an external drive, that doesnt' get a separate drive letter.  A new directory is created (let's say it is /Volumes/DATA_USB) and the USB drive is mounted at that path.  Thus, even though the disk is external to the filesystem, it **looks** like a regular directory (don't be alarmed, there are easy ways to tell if a filesystem is external or not).  

#### Terminal Prompt
`al-laptop:data alexr$`
The terminal prompt tells you a few things:
+ the name of your computer, `al-laptop`
+ the director you are in, `data`
+ your username

#### Recap
+ 'Terminal' is a general word to describe a interactive, text-based mode of computing.
+ 
