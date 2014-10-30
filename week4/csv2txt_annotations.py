# MY ANNOTATIONS OF THE HOMEWORK

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

# open the file READONLY, has to be in the same dir as my .py file
f = open('movies.txt')

# reading one line from the file
# getting rid of the bordering whitespace, splitting it into words
# storing it as a list, 'categories'
categories = f.readline().strip().split(',')

#join the words in categories with a space and print it
print ' '.join(i for i in categories)

#take each line in the rest of the file (note readline() vs readlines())
for line in f.readlines():

    # strip each line of bordering whitespace, separate fields by commas (csv)
    # save as filmData
    filmData = line.strip().split(',')

    # instead of 'for i in filmData', which would give me the fields
    # i'm enumerating filmData so i get NUMBER, FIELD for each field in the line
    for num,val in enumerate(filmData):

        # if a FIELD has no length, aka it's an empty string:
        # change filmData's NUM entry to 'NO VALUE'
        if len(val) == 0:
            filmData[num] = "NO VALUE"

    # i'm zipping the categories and filmData lists into a single
    # list of pairs, like [ (categories[0],filmData[0]),(categories[1],filmData[1]) ... ]
    # then I'm printing the category type, and the corresponding film data
    for category, data in zip(categories,filmData):
        print "%s: %s" % (category,data)
