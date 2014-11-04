import os
import sys
# setup a main loop that displays some menu information

def clearScreen():
    os.system('clear')

def prompt(s=''):
    return raw_input(s)

menu = ['Enter a word','Find a word','Show all words','Update a Word','Delete','Quit']

def mainLoop():

    while True:
        clearScreen()
        for num,option in enumerate(menu):
            print num+1, option

        response = raw_input("please choose an option\n")
        if response in ['q','Q']:
            sys.exit()
        if response in ['1','E','e']:
            insert()
        if response in ['2','F','f']:
            lookup()
        if response in ['3','S','s']:
            showAll()


def insert():
    clearScreen()
    word = prompt("Word:\n")
    definition = prompt("Definition:\n")

    while len(word) == 0 or len(definition) == 0:
        clearScreen()
        print "Sorry, I can't accept empty input. If you want to return to the Menu or Quit, type 'm' or 'q' in any field and press ENTER"
        word = prompt("Word:\n")
        definition = prompt("Definition:\n")
    if word in ['q','Q']:
        sys.exit()
    if word in ['m','M']:
        return
    else:
        clearScreen()
        print word
        print definition
        response = prompt("\nShall I commit %s to the database?" % word)
        if response in ['y','Y']:
            successful,msg = dbCommit(word,definition)
            if successful:
                prompt('successful')
            else:
                print msg

def dbCommit(word,definition):
    f = open('default.db','a')
    f.write(''.join([word,',',definition,'\n']))
    f.close()
    return True,"success"


def lookup():
    clearScreen()
    response = prompt("Which word would you like to look up?\n")
    query(response)

def query(word):
    f = open('default.db','r')
    content = f.readlines()
    f.close()
    entries = [line.strip().split(',') for line in content]
    for w,d in entries:
        if word == w:
            prompt("definition: %s" % d)
            return
    else:
        prompt("sorry, that word doesn't exist. Hit any key to return to the main menu.")



mainLoop()
