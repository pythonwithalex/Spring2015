#!/usr/bin/env python

# q: how many unique words in sentence?

original = "Thrift is poetic because it is creative; waste is unpoetic because it is waste."
modified = ""
# manually compute answer
# 8 unique words

# filter punctuation out without using control structures
# s = s.replace(';')
# s = s.replace('.')

# filter punctuation not part of a word
exclude = [';',':','/','.','-']

for char in exclude:
  if char in original:
    modified = original.replace(char,'')

# filter punctuation with list comprehensions and ''.join()
# modified = [char for char in original if char not in exclude]
# ''.join(i for i in modified)

# ensure Thrift and thrift are treated the same
modified = modified.lower()

# split words
words = modified.split()
print words

# eliminate duplicates
word_set = set(words)
print word_set

# count unique words
unique_words = len(word_set)
print 'There are {} unique words in the sentence "{}"'.format(unique_words,original)
