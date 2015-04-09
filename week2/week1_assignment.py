#!/usr/bin/env python
# Steps
# 1.  compute answer mentally so we can verify our code works
# 2.  filter punctuation out without using control structures
# 3.  filter punctuation not part of a word
# 4.  ensure Thrift and thrift are treated the same
# 5.  split words
# 6.  eliminate duplicates
# 7.  count unique words


# q: how many unique words in sentence?

original = "Thrift is poetic because it is creative; waste is unpoetic because it is waste."
modified = original[:]

# manually compute answer
# 8 unique words

# filter punctuation out without using control structures
# s = s.replace(';')
# s = s.replace('.')

# filter punctuation not part of a word
exclude = [';',':','/','.','-']

for char in exclude:
  if char in original:
    modified = modified.replace(char,'')
    print modified

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

# rebuild original sentence from modified one
modified = list(modified)
semi_index = original.index(';')
dot_index = original.index('.')
modified.insert(semi_index,';')
modified.insert(dot_index,'.')
modified = ''.join(i for i in modified)
modified = modified.capitalize()
print "Is our modified string equal in value to our original string? {}".format(modified == original)
