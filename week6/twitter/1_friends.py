#!/usr/bin/env python

# Note: If you get an InsecurePlatformWarning, you can run 'python -W ignore <python file>' to silence them temporarily.
# WARNING: he he ... the warnings are there for your benefit, so don't ignore them in your normal development context.

import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


friend_objs = [ friend for friend in tweepy.Cursor(api.friends).items() ]

# The list comprehension above is equivalent to :
# for friend in tweepy.Cursor(api.friends).items():
#     print friend

print 'you have {} friends on twitter'.format(len(friend_objs))
for friend in tweepy.Cursor(api.friends).items():
    print('+ {}'.format(friend.name))
