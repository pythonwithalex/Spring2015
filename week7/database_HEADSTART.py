class Database:

    def __init__(self,db_file):
        self.db_file = db_file
  	
	def store(self,w,d):
		f = open(self.db_file,'a')
		f.writelines(''.join([w,',',d,'\n']))
		f.flush()
		f.close()
		
db = Database('default.db')
word = raw_input("enter a word:\n")
definition = raw_input("enter a definition:\n")
db.store(word,definition)
