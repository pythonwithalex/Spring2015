#!/usr/bin/env python

# this script will eventually get all the tweets in temporal order
# for the duration of a redsox game

# now it gives you all tweets for the whole day of the game

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
                       since_id="2015-05-13 04:00:00",
                       until="2015-05-14 00:00:00",
                       ).items()

for tweet in tweets:
  tweet_file.write('{}\n{}\n\n'.format(tweet.created_at,\
                                       tweet.text.encode('utf-8')))
tweet_file.close()
