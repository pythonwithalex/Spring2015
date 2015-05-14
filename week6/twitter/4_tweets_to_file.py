# get a Twitter API key

# run this as 'python script.py > output.txt' to store the json data in a file 
import tweepy
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

max_tweets=100
query='#redsox'
tweets = [status._json for status in tweepy.Cursor(api.search, since_id="2015-05-13",until="2015-05-14", q=query).items(max_tweets)]

#tweet_file = open('output.txt','w')
tweet_count = 0

for tweet in tweets:
  print tweet
