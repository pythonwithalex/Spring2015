#!/usr/bin/env python

# open the database
f = open('posts.md','r')

# read file line by line into a list called 'content'
content = f.readlines()

# close file
f.close()

# same as f = open, but safer and you don't need to close the file
with f as open('posts.md','r'):
  content = f.readlines()

# remove empty lines
filtered_content = [line for line in content if len(line.strip())]

# strip whitespace from each line
filtered_content = [line.strip() for line in filtered_content]

# filter out titles and put in separate list
titles = filtered_content[::2]

# filter out content and put in separate list
content = filtered_content[1::2]

# test content
# content[0]
# content[1]
# content[2]
# content[3]

# join title and content lists into one list of [title,content] lists
posts = zip(titles,content)

# print out each post in a nicely formatted way
for post in posts:
  print 'title:{}\ncontent:{}'.format(post[0],post[1])

# add dates after each content section in the post file (not shown here)

# create a third list for dates
dates = filtered_content[1::3]

# fix other lists to account for new structure [::3]

# update our use of zip to include dates list
posts = zip(titles,content,dates)

# verify we have the right structure after the changes



# now write a few functions to encapsulate this functionality
# load posts
# newest post


