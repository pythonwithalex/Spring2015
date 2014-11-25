class customString:
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

if __name__ == '__main__':

    v = customString('alex')
    v.length()
    v.scramble()
    print v.addToMe(' is a cool dude.')
