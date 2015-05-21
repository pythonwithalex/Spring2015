# coding: utf-8

import tweepy
import json


''' 
    The goal here is to print out the words in Slavoj Zizek's most recent tweets in descending order by frequency.
'''

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = [tweet._json 
          for tweet 
          in api.user_timeline('Slavojiek',count=200)]

def pare(word):
    '''chars to remove from the left or right side of the word'''
    rm_chars = (' ',
                ',',
                '.',
                "'",
                '"',
                ";",
                "?",
                "#",
                "@",
                "?",
                "$",
                "&",
                "‘"
          )
    for i in rm_chars:
        word = word.strip(i)    
    return word
    
def is_valid(word):
    ''' some basic criteria to exclude non-words'''
    rv = True
    if not len(word):
        rv = False
    if len([c for c in word if c.isalpha()]) < (len(word)/2):
        rv = False
    if 'http://' in word:
        rv = False
    return rv

def sort_by_count(two_tuple):
    ''' Key function used in sorted below. 
        returns the word's count.
    '''
    return two_tuple[1]

tweets_text = [tweet['text'] 
               for tweet in tweets 
               if not tweet['retweeted']  # if it's standard tweet
               and 'RT @' not in tweet['text']] # AND it doesn't have RT in text

# collect all *valid* words in the tweets from 'tweets_text' in one list
# also, remove characters not part of the word ( done with pare(word) )
words = [ pare(word.encode('utf-8')) 
            for line in tweets_text
            for word in line.split() if is_valid(word.encode('utf-8')) ]

# turn this list into a set, aka eliminate duplicates
words_set = set(words)

# this will hold the word and its count as a tuple: (word,count)
results = []

# for each unique word, append a tuple of that word
# and the count of that unique word in the words list (which has the duplicates)
for word in words_set:
    results.append((word, words.count(word)))

# sort the data list of tuples by each tuple's second key
# this is where my sorted_by_count key function comes in
words_desc = sorted(results,key=sort_by_count,reverse=True)

# get the most popular count 
highest_count = words_desc[0][1]

# print it all out
for word in words_desc:
    print '{}: {}'.format(*word)
    # note: '*' expands a collection into its individual elements (not a tuple)
    # equiv to word[0],word[1]
    # Works when passing values to a function
    # not the same as word[:], which gives you a copy of word, a tuple
