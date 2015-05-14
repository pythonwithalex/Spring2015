#!/usr/bin/env python

# Note: If you get an InsecurePlatformWarning, you can run 'python -W ignore <python file>' to silence them temporarily.
# WARNING: he he ... the warnings are there for your benefit, so don't ignore them in your normal development context.

import tweepy
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


my_details = api.me()
my_dtails_json = json.dumps(my_details,sort_keys=True)
