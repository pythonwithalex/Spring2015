#!/usr/bin/env python

# this gets all the tweets in temporal order
# for the duration of a redsox game

# Tasks: sort, deduplicate, print out most frequent words

# steps:

# get a Twitter API key
# search for #redsox hashtag 

import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet_file = open('output.txt','w')
tweet_count = 0

tweets = tweepy.Cursor(api.search,q="#redsox",\
                       lang="en",
                       since_id="2015-05-13",
                       until="2015-05-14",
                       ).items()

for tweet in tweets:
  tweet_file.write('{}\n{}\n\n'.format(tweet.created_at,\
                                       tweet.text.encode('utf-8')))
tweet_file.close()
