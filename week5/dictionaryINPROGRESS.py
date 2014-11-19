import os

def insert():
    word = raw_input("Please Enter A Word:\n")
    definition = raw_input("Please Enter a Definition\n")
    print "word: ",word
    print "definition: ",definition
    response = raw_input("Does this look okay to you?")
    if response in ['y','Y']:
        store(word,definition)
    
def store(word,definition):
    f = open('default.db','a') # a for append
    f.write(','.join([word,definition+'\n']))
    f.close()

def find():
    queryWord = raw_input("Please Enter a Word To Search For:\n")
    f = open('default.db','r') # 'r' for read
    lines = f.readlines()
    for line in lines:
        if queryWord in line:
            word = line.split(',')[0]
            definition = line.split(',')[1]
            print "\nword:",word
            print "definition:",definition
    raw_input("") # prevents loop from immediately continuing
    f.close()
	
def delete():
    f = open('default.db','rw')
    wordToDelete = raw_input("Please Enter a Word To Delete:\n")
    while True:
        line = f.readline()
        if line is None:
            break
        else:
            print line

	        
    raw_input("") # prevents loop from immediately continuing

    
menuItems = ['Add','Find','Show All','Update','Delete','Quit']

while True:
    os.system('clear')
    for num, item in enumerate(menuItems):
        print num+1,item
    
    response = raw_input("Please Choose a Menu Item\n")
    if response in ['6','Q','q']:
        break
    if response in ['1','A','a']:
        insert()
    if response in ['2','L','l']:
        find()
    if response in ['5','D','d']:
        delete()
