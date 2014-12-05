# exercises: 

# sentence = "I went to work today." 
# words = sentence.split() 

# ['I went t', ' w', 'rk t', 'day'] 

# words2 = sentence.split('o') 
# ['I went t', ' w', 'rk t', 'day'] 
from datetime import datetime 

# print datetime.now() 

# print datetime.now()[0] 
# now is not a standard string, see ? 

# can't do this with date time because it isn't a standard python string obj 
# TypeError: 'datetime.datetime' object has no attribute '__getitem__' 
# let's convert it to a string 

now = str(datetime.now()) 
#print now[:] 

# this means that the string we created has a slice method now 
# makes sense since all strings have the internal method called __get__item 

# let's turn this into something we can use 
# i'm going to assign certain values to variables 

# if this is the string '2014-10-07 11:41:59.772349' 
# then i want to call the first chunk 'calendar' 
# and the second chunk 'clock' 
calendar, clock = now.split(' ') 

# but let's break the clock component up into something more readable 
# i'm thinking hours and minutes, no milliseconds needed 
# so... 
# split the clock string at the dot 
# take the left hand side 
hour, minute = clock.split('.')[0].split(':')[:2] 
print "It is " + hour + ":" + minute + " on " + calendar 
