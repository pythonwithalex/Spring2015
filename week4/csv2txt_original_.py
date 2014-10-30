# PWP week 3 Assignment: FIX MY CSV2TXT FUNCTION
#
# 1: Comment each line with a succinct description of what you think
#    it's doing.  If you don't know, try looking into it.
#
# 2: Write some code to format the file like this:

#    TITLE              DIRECTOR             RATING
#    Wayne's World      Penelope Spheeris    Rating: Excellent
#    Slam Dunk Ernest   John R. Cherry III   Rating: 2 points
#    ...
#
#
#    Hints: you can use len() and a width variable fruitfully here.
#
# 3: Fix or improve anything you think needs attention if you feel comfortable.


import sys

f = open('movies.txt')
categories = f.readline().strip().split(',')
print ' '.join(i for i in categories)
for line in f.readlines():
    filmData = line.strip().split(',')
    # putting brackets around a 4, like [4]
    # initializes a list with the number 4 in it
    for num,val in enumerate(filmData):
        if len(val) == 0:
            filmData[num] = "NO VALUE"
    for category, data in zip(categories,filmData):
        print "%s: %s" % (category,data)
