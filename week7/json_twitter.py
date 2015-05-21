import tweepy
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = [tweet._json for tweet in api.user_timeline('Slavojiek',count=200)]
tweets_text = [tweet['text'] for tweet in tweets]

def pare(word):
    rm_chars = (' ',
                ',',
                '.',
                "'",
                '"',
                ";",
                "?",
                "#",
                "@",
                "?",
                "$",
                "&",
                "‘"
                    )
    for i in rm_chars:
        word = word.strip(i)    

    return word

def is_valid(word):
    rv = True
    if not len(word):
        rv = False
    if len([c for c in word if c.isalpha()]) < (len(word)/2):
        rv = False
    if 'RT\t@' in word:
        rv = False
    if 'http://' in word:
        rv = False
    return rv
