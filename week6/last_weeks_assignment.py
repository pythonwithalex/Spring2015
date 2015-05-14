#!/usr/bin/env python

words = [
	'representative', 
	'numeric', 
	'senile', 
	'effluent', 
	'ear', 
	'bespectacled' , 
	'elegiac',
	'ex-developer' 
	]

def count_e(s):
  return s.count('e')
  
sorted_words = sorted(words,key=count_e,reverse=True)

for word in sorted_words:
  print word, word.count('e')
