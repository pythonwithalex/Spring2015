#!/usr/bin/env python

f = open('posts.md','r')
content = f.readlines()
filtered_content = [line for line in content if len(line.strip())]
filtered_content = [line.strip() for line in filtered_content]
titles = filtered_content[::2]
content = filtered_content[1::2]
# content[0]
# content[1]
# content[2]
# content[3]
posts = zip(titles,content)
for post in posts:
  print 'title:{}\ncontent:{}'.format(post[0],post[1])
