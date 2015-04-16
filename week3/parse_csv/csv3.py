#!/usr/bin/env python

# notes: using built-in 'ljust' as a replacement for calc_padding

# To Do: ???

max_field_len = 0
width = 0
content = []
header = []
data = []

def calc_padding(max_width,s):
    '''
    returns a string padded with whitespace so that total length equals max_width 
    '''
    padding_size = max_width - len(s)
    padding = ' '*padding_size
    padded_string = s + padding
    return padded_string

f = open('MOCK_DATA.csv')
for line in f.readlines():
  line = line.strip()
  content.append(line) 
f.close()

header = content[0].split(',')
for line in content[1:]:
  data.append(line.split(','))

for item in header:
  if len(item) > max_field_len:
    max_field_len = len(item)

for row in data:
  for item in row:
    if len(item) > max_field_len:
      max_field_len = len(item)

width = max_field_len + 1

print ''.join(item.ljust(width) for item in header)
for line in data:
  print ''.join(item.ljust(width)  for item in line)
