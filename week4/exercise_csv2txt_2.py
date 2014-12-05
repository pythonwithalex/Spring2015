# MY FIRST REVISION OF CSV2TXT.PY

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

# 4: NOTE, I changed the movies.txt file to get rid of the special character
# in Nobuhiko Obayashi's name.  This fixed an alignment issue.

import sys

def columnFormat(width,data):
    # prints a correctly formatted line from a sequence
    # using the equation "whitespace buffer equals column size minus string length"
    string_elements = []
    for i in data:
        buffer = (width-len(i))*' '
        string_elements.append(i)
        string_elements.append(buffer)
    return ' '.join(i for i in string_elements)

WIDTH = 25

# this is how you open a file called 'movies.txt' for READING
f = open('movies.txt')


# lets create a list called categories that takes the result of
# reading the FIRST line from the csv file, stripping the whitespace, and splitting into a sequence
# Im' assuming the first line has header information

categories = f.readline().strip().split(',')

# let's print this now, accounting for the width of each category word
print columnFormat(WIDTH,categories)

for line in f.readlines():
# for the rest of the lines (i'm assuming these are data):

# filmData is a list that is created from each line read from the file
# NOTE: a line will often have the '\n' character at the end, which when printed
# makes the subsequent output print on the next line

    # a list comprehension is easiest here, though they can be difficult at first
    # for word in process(line)
    # give me process(word)
    # make this output a list ( this is what [] does)
    filmData = [word.strip() for word in line.strip().split(',')]


    for num,val in enumerate(filmData):
    # filmData is a list of three things, so num will be 0,1,2 and val will be item 1,2 or 3
    # if a list sequence item is just an empty string, replace it with the text 'NO VALUE'
    # this gives us
    # num  val
    #  0   Wayne's world
    #  1   Penelope Spheeris
    #  2   Excellent.
        if len(val) == 0:
            filmData[num] = "NO VALUE"

    print columnFormat(WIDTH,filmData)

## NOTE:    
##  below is why I wrote a separate function to handle the formatting
##  take a look > V
##                V
##                V

##    print filmData[0].strip(),(w-len(filmData[0]))*' ',filmData[1].strip(),(w-len(filmData[1]))*' ',filmData[2]
