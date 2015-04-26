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

An important part of using a shell is understanding how the system's files are organized. Mac OS X is more or less part of the Unix-like family of Operating Systems and thus its files are arranged in accordance with the Filesystem Hierarchy Standard.  In order to avoid boring you to death, just know that this means that the filesystem follows a standard that makes it easy to locate common and essential files (standards are good: they make your job as a developer much simpler).  Also, most importanly for us, this means that the Mac OS X filesystem can be visualized as a single tree (well, an upside-down tree).  The 'root' of the tree is at the top and is considered the outer-most directory in that everything else is treated as if it's inside the root.  Inside the 'root' directory is a directory called /Users.  Inside /Users is the Student directory.  Inside /Student are Documents, Desktop, Pictures, etc.  Inside Desktop or Documents, we store our Python files. 

````
                          /
                 
   /Users               /Volumes                    /System   
     /Student             /Time Machine Backups       ....
       /Desktop
         lists.py
       /Documents
         csvparser.py
````

**Note**: On a Windows machine, you will have a C drive and maybe a D drive if you have a separate data partition, and if you mount an external drive, that will have be organized under a new, separate drive letter, maybe Z.  Unix-like filesystems don't do this.  Since the '/' directory, aka the root directory, is the very top-level of the filesystem.  If we mount an external drive (a Time Machine disk, a USB drive), that doesn't get a separate drive letter like it would on a Windows machine.  Instead, a new directory is automatically created (let's say it is /Volumes/DATA_USB) and the USB drive is mounted at that path.  We can navigate to the external disk's files just like any other directory on the machine. Even though the disk is external to the system's bootable filesystem, it **looks** like a regular directory.  Don't be alarmed, though, there are easy ways to tell if a filesystem is external or not (hint: try the `df` command).  

#### Terminal Prompt

The terminal prompt looks like this: `al-laptop:data alexr$`

It tells you some useful things in a pretty compact way:

+ the hostname of your computer, `al-laptop`
+ the directory you are in, `data`
+ your username, `alexr`
+ What type of user you are: `$` means you are a regular user.  You don't have access to all files, just those that you own.

#### Some Useful Commands

**the date**

````bash
al-laptop:data alexr$ date
Sun Apr 26 11:53:02 EDT 2015
````

**the hostname of your computer**

````bash
al-laptop:data alexr$ hostname
al-laptop.local
````

** the directory you are in **

````bash
al-laptop:data alexr$ pwd
/data
al-laptop:data alexr$
````

** change into a different directory **

````bash
al-laptop:data alexr$ cd python
al-laptop:python alexr$ 
````

** the files in your current directory **

````bash
al-laptop:python alexr$ ls
algorithms_in_python.pdf
curses_base.py
davidMertz-python-Functional-Programming.pdf
dive-into-python3.pdf
django_1.6_docs.pdf
flask-docs.pdf
hackingciphers.pdf
head_first_python.pdf
magicmethods.pdf
makinggames.pdf
oop_general
pptrs.pdf
python_building_machine_learning_systems.pdf
python_highperformance.pdf
pythonexcel.pdf
text_processing_in_python.pdf
textprocessing_davidmertz.pdf
thinkbayes.pdf
thinkpython.pdf
writing_idiomatic_python_3.pdf
al-laptop:python alexr$ 
````
