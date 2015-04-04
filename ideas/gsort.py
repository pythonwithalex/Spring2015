#!/usr/bin/env python
from sys import argv, exit

def getKey(item):
  return item.lower()[2]

def gsort(filename=None):
  '''
  gsort(filename=None)
  Sorts a structured list of glossary terms. 
  Each line begins with '+ ', but this shouldn't affect the sort. 
  '''
  if not filename:
    filename = argv[1]
  with open(filename) as f:
    all_lines = f.readlines()
    header,content = all_lines[0],all_lines[1:]
    content = [ line for line in content if line.strip() ]
    content = sorted(content, key=getKey)

  for line in content: 
    print line

if __name__ == '__main__':

  if len(argv) != 2:
    print "Usage: gsort <input file>"
    exit(1)

  gsort()

else:
  print 'imported'
