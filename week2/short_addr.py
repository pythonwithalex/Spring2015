# Programming With Python Week 2  
# Writing a flexible version of the id() function

# Backstory: the id() function tells us the memory address of a variable.
# All variables need to be stored somewhere, am I right!?
# 
# An operating system puts them in RAM, which you can think of as a long
# line of places to put data: | 1 | 2 | 3 | 4 | 5 ... etc.

# here's an example:
# If you have a line like s = 'Michael Jordan' in your Python file 
# and then you run the program, the computer says to itself:
#
#     Where do I have free space?
#     Oh, I have free space at 4299245408, let's put this 'Michael Jordan'
#     string at that address. 
#
# As you can tell, the memory address of a variable is a pretty long number.
# 
# For us, the point of using the id() function is to simply compare whether 
# the memory address of two different variables is the same. When we do
#
#     w = 'word'
#     w = 'words'
#
# is the memory address of 'w' the same? We'll find out.


# But first, let's take id() and use it in a more convenient way.
# The numbers id() gives us are long and really only need the 
# last few characters, so ...

# Let's write a function that just gives us the last NUM digits, where
# NUM is an integer variable.

# Version 1 #

# s = 'Michael Jordan'

# def short_addr(obj):
#     print id(obj)

# short_addr(s)



# Version 2 #

# s = 'Michael Jordan'

# def short_addr(obj):
#     print str(id(obj))[-4:]

# short_addr(s)


# Version 3 # 
# s = 'Michael Jordan'

# def short_addr(obj,n):
#     print str(id(obj))[-n:]

# short_addr(s)



# Version 4 #

# s = 'Michael Jordan'

# def short_addr(obj,n=4):
#     print str(id(obj))[-n:]

# short_addr(s)




# Version 5 #
def short_addr(obj,num=4):
    if num > len(str(id(obj))):
        print "num exceeds length of string."
    elif num < 0:
        print 'The number must be positive.'
    else:
        short_addr = str(id(obj))[-num:]
        print short_addr

