#!/usr/bin/env python

import json
import tweepy

api_key = 'WZmlMvlVJxBBx1Vqod2uK8Mkz'
api_secret = 'LrjmQCNANcFHnPXQPYlAPQPqpQdwWcODy7C7IdoPxGhmyimfGR'
auth_key = '3115539945-0zUyYKeGga8oQiY3JOlSgJ6czdJVlt4rEOgY9up'
auth_secret = 'mQBaKib64VpSMdSFlqS3saBOvm62JySkn6CsX8Egrm3wa'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(auth_key, auth_secret)

api = tweepy.API(auth)

out_file = open('output.txt','w')

redsox_tweets = tweepy.Cursor(api.search,q="#redsox",\
                       since_id="2015-05-13",
                       until="2015-05-14",
                       ).items()


for tweet in redsox_tweets:
  line = '{}\n{}\n\n'.format(tweet.created_at,\
                            tweet.text.encode('utf-8')
                           )
                         
  out_file.write(line)
