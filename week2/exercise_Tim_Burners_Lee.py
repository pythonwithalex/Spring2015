s = "Tim Berners-Lee, the creator of the World Wide Web, has big plans for the future of the Internet. Greater use of online data, faster computers to take care of day-to-day tasks and more collaboration among people around the world are all possible, Berners-Lee told an audience at a technology conference here on Wednesday. But the British computer scientist warned that this future would happen only if people continued to have unfettered access to the basic infrastructure that powers the Internet."

words = s.split()
for num,val in enumerate(words):
    print "%d %s" % (num,val)

print "word count: ", len(words)
