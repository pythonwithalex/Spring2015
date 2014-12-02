import os

class Database:

    # store the database file name
    def __init__(self,db_file):
        self.db_file = db_file
  	
    def insert(self,w,d):
        with open(self.db_file,'a') as f:
            f.writelines(''.join([w,',',d,'\n']))
            # with construct does f.flush() for us
            # f.flush() makes sure Python run-time buffer
            # writes data to OS buffer
            os.fsync(f) # makes sure OS writes data to file
                        # doing this because it helps ensure db integrity
	    return True	

    def find(self,w):
        # new way of safely opening files
        results = []
        with open(self.db_file,'r') as f:
            lines=f.readlines()
            for line in lines:
                word, definition = line.strip().split(',')
                if w in word:
                    results.append([word,definition])
 
        return results

    def dump(self):
        with open(self.db_file,'r') as f:
            return [line.strip().split(',') for line in f.readlines()]

    def update(self,w,new_d):
        # open file for reading
        with open('default.db','r') as f:
            lines=f.readlines()
            for num,line in enumerate(lines):
                word,definition = line.strip().split(',')
                if w == word:
                    definition = new_d
                    lines[num] = word + ',' + definition + '\n'

        with open('default.db','w') as f:
            f.writelines(lines)

        #fix the return value logic so it returns false if no word found
        return True

    def delete(self,w,new_d):

        filtered_lines = []

        # open file for reading
        with open('default.db','r') as f:
            lines=f.readlines()
            for num,line in enumerate(lines):
                # break lines into word, def
                word,definition = line.strip().split(',')
                # filter out lines with word that match
                if w != word:
                    filtered_lines.append(line)
        
        with open('default.db','w') as f:
            f.writelines(filtered_lines)
    #fix the return so it returns false if no word found
        return True

if __name__ == '__main__':
    db = Database('default.db')
    print db.insert('a','z')
    print db.update('a','b')
    print db.dump()
    print db.delete('a','b')
