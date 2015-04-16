#!/usr/bin/env python

# attempt #1.  
# we read the file and just the header is 'prettified'

content = []
f = open('MOCK_DATA.csv')
for line in f.readlines():
  line = line.strip()
  content.append(line) 
f.close()

header = content[0] # a string
data = content[1:] # a list of strings

print header.replace(',',' | ')
print ' '
for line in data:
  print line
