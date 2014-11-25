### DICTIONARY APPLICATION NOTES

#### To start, copy [week 5 dictionary file](../week5/dictionaryINPROGRESS.py) into TextWrangler 

Testing it Out

	Test the app out for a few minutes and see what works, what doesn't

	What is Nonfunctional?
	What can be improved?
	Looking at the code, what can be improved?


Add a FindAll Function

	1) open file for reading
	2) readlines into list
	3) split lines into word,def
	4) print word,def

Deleting Words from the Dictionary
	
	Problems so Far:
	
	1) finding word in file and updating it is hazardous

	2) finding word in a list constructed from the file is fine,
	but deleting it is tricky

	Solution?
	
	1) take the list constructed from file and copy it into a new list,
	but filter what you don't want

Updating Words in the Dictionary
	
	1) read file into list called lines
	
	2) use enumerate too loop through lines
	
	3) if a line.split(',')[0] matches the word to update
		+ show current word and def
		+ get user input for revision
		+ if that is > 0 in length, modify lines[num] with new string
		+ use ''.join(i for i in [word,' , ',new_definition,'\n']) to match format

Writing a Database Object

	1) create separate file called database.py (lowercase d)

	2) Functionality?
		initialize variables
		display which file it's using
		find a word
		find all words
		delete a word
		update a word
		(same funcs from our previous program, but bound to the db obj)

	3) class Database:
	(notice Database is capitalized, per convention

	4) __init__ method
	
	class Database:
		def __init__(self,db_name):
			self.db_name = db_name
	
	5) Define your database class and give it an init method that takes in a filename
	and stores it as self.db_file
	
	6) Write a getDbName() function that prints self.db_file

	7) go to the main file and outside of any function, create the global database object (call it db). 

	Review: 
		database.py file is 'database'
		Database is the class
		db = Database('default.db') -> db is object
		there is no db object until we assign the name db to the result of the Database() class initialization function.

