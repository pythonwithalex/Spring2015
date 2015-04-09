#!/usr/bin/env python

# q: how many unique words in sentence?

s = "Thrift is poetic because it is creative; waste is unpoetic because it is wa
ste."

# manually compute answer
# 8 unique words

# filter punctuation not part of a word
exclude = [';',':','/','.','-']

for char in exclude:
  if char in s:
    s = s.replace(char,'')

# ensure Thrift and thrift are treated the same
s = s.lower()

# split words
words = s.split()
print words

# eliminate duplicates
word_set = set(words)
print word_set

# count unique words
print len(word_set)
