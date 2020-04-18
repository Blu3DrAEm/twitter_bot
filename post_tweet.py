# twitter_bot
# Josh Anderson 6/17/2020
# goal: post tweet

import tweepy

consumer_key = '...' # Generate your own API keys at https://developer.twitter.com/apps
consumer_secret = '...'# 
access_token = '...'
access_token_secret = '...'

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None

oauth = OAuth()
api = tweepy.API(oauth)

api.update_status("I am posting a tweet using Python #Blu3DrÆm")
print('a tweet posted')
