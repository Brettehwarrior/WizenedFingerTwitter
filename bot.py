import json
import tweepy

# Load API key data
keys = {}
with open('keys.json', 'r') as file:
    keys = json.load(file)

# API object
auth = tweepy.OAuthHandler(keys['api-key'], keys['api-secret-key'])
auth.set_access_token(keys['access-token'], keys['access-token-secret'])
api = tweepy.API(auth)

def get_mentions():
    return api.mentions_timeline()

def send_tweet(message:str) -> int:
    """Send tweet with message and return ID"""
    tweet = api.update_status(message)
    print(f'Sent tweet with id {id}')
    return tweet.id