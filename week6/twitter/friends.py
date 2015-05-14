#!/usr/bin/env python

import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# the Cursor is what lets you navigate the api 
for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    print(friend.name)
