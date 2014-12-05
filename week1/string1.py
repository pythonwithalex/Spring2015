# Programming with Python 
# Fall 2014 
# Class 1 Notes 

# Please note: these notes don't include 'q.find' or 'q.join' 
# but we will revisit these. 

# MANUAL VERSION (just the algorithm) 

# 1.you have a word, ie. a bunch of letters 
# 2. find a space for the new word 
# 3. take the last letter of the original word 
# and put it below and to the right of any letters that 
# are already there. 
# 4. repeat until no letters are left in the original word 

# LETS CONVERT THIS INTO PYTHON 

# FIRST, WHAT ARE STRINGS? HOW ARE THEY USED? 
# a string is a sequence of characters surrounded in quotes. 
# "dog", "999999999", " ", "\n" ... these are all strings 

# WHAT PROPERTIES DOES A STRING HAVE THAT WE CAN TAKE ADVANTAGE OF? 

# it has length, aka number of elements 
# it is made up of a sequence of values 
# so.... 
# we can give each element a unique index 
# we access elements in a string like this <string>[position] 

# open ipython and type print 'quick'[] 
# then put in the position that you think corresponds to FIRST LETTER, 'q' 
# hit enter 

# are you surpised at the result ? 
# can you offer a possible explanation for it? 
# try this out further with other numbers 

# VOCABULARY BREAK: position in computer science is more often called 'index'. 

# A string's index is determined in offsets. 
# an offset is the distance from 0, the start of the data. 

# 'quick'[0] is 'q' because we don't need to go anywhere to get q. 
# 'quick'[1] is 'u' because we need to offset 1 unit from the beginning 
# to get to index 1. 

# maybe this is a good way to envision a string (numbers over the '|'s) 
# 0 1 2 3 4 
# |q|u|i|c|k| 
# the numbers are where each element starts. 
# this makes sense, why? 
# 
# my explanation: 
# a value isn't a concrete object like a baseball bat where you can 
# hold it and ostensibly use it from whichever end you want (not good advice, I admit). 
# a value must be READ by a computer from start to end 
# to do this it needs a location where it can start reading. 
# quick[0] is such a location. 

# let's think for a minute of the relationship between the length of a string 
# and the name of its last index 

# with quick, the length is 5. 
print len('quick') 
# but the last index is 4 
print 'quick'[4] 

# so... 
# the last element is the length - 1 
print 'quick'[len('quick')-1] 

# in TextWrangler, type 'quick'[] five times and fill in the index values 
# so that they descend from highest to lowest. 

# let's run this ! 
print 'quick'[4] 
print 'quick'[3] 
print 'quick'[2] 
print 'quick'[1] 
print 'quick'[0] 

# WHY IS THIS BAD? 
# number of lines of code is proportional to the string length! 
# we had to do it manually 
# didn't use any variables 

# 
#	ATTEMPT 2 
q = 'quick' 
print q[4],q[3],q[2],q[1],q[0] 

# THIS IS BETTER, WHY? 
# we used a variable 
# two lines long 
# it prints the results in a more readable way 

# NEEDS IMPROVEMENT, why? 
# we still had to type five string indices 
# there are spaces between the letters 

# ATTEMPT 3 SLICING 
# strings support something called slicing 
# slicing is built on the idea of position 
# <string>[start_position:end_position:step] 
# NOTE: end position is not inclusive so [0:1] means 
# "give me from 0th element up to but not including the first" 
# here are some examples 
print q[:] 
print q[:1] 
print q[-1] 
print q[::1] 
print q[::2] 

# let's try out using negative values 
print q[-1] 
print q[-1:0] 
print q[::1] 

# how do we print a string backwards then? 
# HINT: remember the step argument. try that with a negative... 
# 
# print q[::-1] 
