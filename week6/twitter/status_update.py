#!/usr/bin/env python

import tweepy

api_key = ''
api_secret = ''
auth_key = ''
auth_secret = ''

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(auth_key, auth_secret)

api = tweepy.API(auth)

api.update_status(status="Python is cool #python #cool") 
