# always import standard library modules first
import os
import re


def clearScreen():
    os.system('clear')

# add one word 
def insert():

    clearScreen()
    word = raw_input("Please Enter A Word:\n")
    definition = raw_input("Please Enter a Definition\n")
    clearScreen()

    if len(word) < 1:
        insert()

    else:
        print "word: ",word
        print "definition: ",definition
        response = raw_input("\nDoes this look okay to you?\n")
        if response in ['y','Y','']:
            store(word,definition)
        

# append to the file a comma-delimited string
def store(word,definition):

    # buffer file
    f = open('default.db','a') # a for append
    f.write(','.join([word,definition+'\n']))
    f.close()

def find():

    clearScreen()
    
    # open the file, read into list of lines, close file
    f = open('default.db','r') # 'r' for read
    lines = f.readlines()
    f.close()

    # get query from user
    queryWord = raw_input("Please Enter a Word To Search For:\n")
    
    # split each line by ',' and assign results to word,def
    # if queryWord found in line, split line into word,def and print
    clearScreen()
    print "Search Results:\n"
    for line in lines:
        word,definition = line.split(',')
        if queryWord in word:
            print "\nword:",word
            print "definition:",definition

    raw_input("") # prevents loop from immediately continuing

def showAll():

    clearScreen()
    print "Dictionary Entries"

    f=open('default.db','r')            # open file for reading
    lines = f.readlines()               # save lines of file as list
    f.close()

    for line in lines:                      # for each line
        word,definition = line.split(',')   # split into word,def
        print "\nword:",word                # print each word,def
        print "definition:",definition      # 
    raw_input("")                           # prevents loop from immediately continuing


def delete():

    wordToDelete = raw_input("Please Enter a Word To Delete:\n").strip()
    f = open('default.db','r')          # open db file
    lines = f.readlines()               # read lines into temporary list
    lines_copy = []
    f.close()

    # note on the following method:
    #   deleting a list element while iterating through it isn't a easy task
    #   because if you are using the index to locate items to delete, 
    #   that index changes each time you delete an element

    # an easier way is to use a list comprehension like the next python line
    # it filters lines to give me just the lines without the wordToDelete
    # so, in short, i'm copying the list i read from the file into a new, filtered list (lines_copy)
    lines_copy = [line for line in lines if wordToDelete not in line]


    f = open('default.db','w')          # open file again for writing
    f.writelines(lines_copy)                 # overwrite file with modified list    f.flush()                           # back
    f.close()                           # close the file

    raw_input("")               # prevents loop from immediately continuing


def main():

    menuItems = ['Add','Find','Show All','Update','Delete','Quit']
    
    while True:
        clearScreen()
        for num, item in enumerate(menuItems):
            print num+1,item
        
        response = raw_input("\nPlease Choose a Menu Item\n")
        if response in ['6','Q','q']:
            break
        if response in ['1','A','a']:
            insert()
        if response in ['2','f','f']:
            find()
        if response in ['3','A','A']:
            showAll()
        if response in ['5','D','d']:
            delete()

main()
