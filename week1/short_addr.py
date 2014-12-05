# week 2 - writing a flexible version of the id() function 

# Backstory: the id() function tells us the memory address of a variable. 
# All variables are stored somewhere, am I right!? 
# 
# A computer naturally stores them as numbers. 
# 
# here's an example: 
# If you have a line like s = 'Michael Jordan' in your Python file 
# and then you run the program, the computer says to itself: 
# 
# Where do I have free space? 
# Oh, I have free space at 4299245408, let's put this 'Michael Jordan' 
# at that address. 
# 
# As you can tell, the memory address of a variable is a long number. 


# So to recap, we're writing a function that checks the last NUM digits 
# of the object whose location we care about. 

# here's an example variable: 
# s = 'Michael Jordan' 

def short_addr(obj,num=4): 
    '''converts id(obj) to a string and prints the last n digits''' 

    if num > len(str(id(obj))): 
        print "to whom it may concern:\n the number you have supplied"
        "is unfortunately greater than the length of" 
        "the string itself!" 
    elif num < 0: 
        print 'number must be positive' 
    else: 
        short_addr = str(id(obj))[-num:] 
        print short_addr 
