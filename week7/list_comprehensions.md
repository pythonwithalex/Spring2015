## Ways to make List Comprehensions Easier to Write and Reason about 



````python

# assume i have a list of first names in a list called 'first_names'

long_first_names = [ name
                     for name in first_names
                     if len(name) > 8 ]
                     
                     
````

Double List comprehension - Converting a bunch of sentences into a set of words

````python
#  assume I have a list of sentences and 
words = [ word.strip() 
            for line in tweets_text
            for word in line.split() if is_valid(word) ]

````
