# Using a class to define a custom string type

class CustomString:
    def __init__(self, s):
        self.s = s
    def length(self):
        print len(self.s)
        return len(self.s)
    def scramble(self):
        print ''.join( chr(ord(i)+2) for i in self.s)
    def addToMe(self,new_s):
        self.s += new_s
        return self.s

if __name__ == '__main__':   ## conditional makes sure that the following lines run if this file is run by itself
                             ## and not imported from a module.

    v = CustomString('alex') ## this creates the object v by running CustomString.__init__() class function
                             ## v is the result, aka the object
    v.length()  
    v.scramble()
    print v.addToMe(' is a cool dude.')
