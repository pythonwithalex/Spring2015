### Why modifying a list in place is not a good idea

# original list
l=['a','b','c','a','c']

# get indexes of items we want to delete
for num,i in enumerate(l):
    if i == 'a':
        print num
# prints 0
# prints 3

for i in [0,3]:
    del l[i]
    
    
print l
# prints ['b', 'c', 'a']


# Question 1: Why is there an 'a' left, and why are some elements missing?

# Question 2: what do we do instead?
