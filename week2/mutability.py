Programming With Python Week 2
Mutability vs Immutability

If a data type is mutable, parts of it can be changed and it is still the same 'object'.

If a data type is immutable, then you can't change any part.  You can only create an object by the same name and give it different values.


Lists are mutable
#################

l = [0,1,2,3,4]
l.append(5)
print l
[0,1,2,3,4,5]

l is still the same object after I added 5 to it.

Strings are immutable
#####################

s = 'bob'
s = 'robert'

s refers to a new object when you assign it the value 'robert'
