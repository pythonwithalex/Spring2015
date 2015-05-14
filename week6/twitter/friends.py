#!/usr/bin/env python

import tweepy

consumer_key = 'ozimqHNo7fPpSrjwE0tBbYdXn'
consumer_secret = 'OD4ucwCNZ8RCOAHGwfsaEHi1uko9tOapYcF08j8CYN3aMJoY8x'
access_token = '3115539945-umtdlTQzeaIzXa7zg6Ujmu3maIzt2NQkzSpb5fA'
access_token_secret = 'XWEZGdFU10VEZUG9qi0xvgSJ7dpxyvHiilN54A1q5M1oc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    print(friend.name)
