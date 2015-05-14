#!/usr/bin/env python

# resource for api.search
# http://docs.tweepy.org/en/v3.3.0/api.html?highlight=search#API.search

# Exercise: 
# 1) find last redsox game date, (may 13th)
# 2) search for all tweets on the day of that game


import tweepy

consumer_key = 'YOUR_KEY'
consumer_secret = 'YOUR_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# WRITE TWITTER RESULTS TO A FILE
tweet_file = open('output.txt','a')

tweet_count = 0

tweets = tweepy.Cursor(api.search,q="#redsox",\
                       lang="en",
                       since_id="2015-05-13",
                       until="2015-05-14",
                       ).items()

tweet_file.write('time,text\n')
for tweet in tweets:
  tweet_count += 1
  tweet_file.write('{}\n{}\n\n'.format(tweet.created_at,tweet.text.encode('utf-8' )))
tweet_file.close()
print "{} TWEETS".format(tweet_count)
