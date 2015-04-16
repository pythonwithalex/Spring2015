#!/usr/bin/env python
# parse_csv_rev1.py

# purpose:
#   read a csv file and print in a more readable way
#   using tabs in this file

# to do:
#   not well-formatted enough
#   write functions to clean this up



# putting variables i expect to use at top for clarity
max_field_len = 0
width = 0
content = []
header = []
data = []

# Open file, readlines and append to content, same as before
f = open('MOCK_DATA.csv')
for line in f.readlines():
  line = line.strip()
  content.append(line) 
f.close()

# Split header string into a list
header = content[0].split(',')

# For each line after the first, split that line into a list
# and append that list to data
for line in content[1:]:
  data.append(line.split(',')) # a list of lists

# Create a temp string and use it to accumulated previous strings
temp_str = ''
for item in header:
  temp_str = temp_str + (item + '\t') # parenthesis not 'necessary', just clearer


for line in data:
  temp_str = ''
  for item in line:
    temp_str = temp_str + (item + '\t')
  print temp_str
