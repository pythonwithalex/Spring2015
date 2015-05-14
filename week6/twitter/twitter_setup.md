## Twitter Application Setup

Steps you need to do via Twitter.com:

+ register for a twitter account
+ go to apps.twitter.com
+ login
+ create an application
+ get an API key and API secret
+ leave the callback URL blank
+ make up a fake, valid url for the website field
+ generate the auth key and the auth secret

Setup code in your application:

````python
import tweepy

# paste the keys you got from apps.twitter.com into the string quotes below
consumer_key = ''
consumer_secret = ''
auth_key = ''
auth_secret = '' 

# Here, we need to create an OAuth authentication object using our consumer key and secret
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create our api object using the secret stuff above
# this is our our-handle on the twitter stream
api = tweepy.API(auth)

````
