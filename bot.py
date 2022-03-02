from time import sleep
from EldenRingMessage import message
import schedule
import json
import tweepy

USER_ID = 1499033585222836230

# Prepare message stuff
message_data = message.messages()
message_factory = message.MessageFactory(message_data)

# Load API key data
keys = {}
with open('keys.json', 'r') as file:
    keys = json.load(file)

# API object
auth = tweepy.OAuthHandler(keys['api-key'], keys['api-secret-key'])
auth.set_access_token(keys['access-token'], keys['access-token-secret'])
api = tweepy.API(auth)
tag = f"@{api.get_user(user_id=USER_ID).screen_name}"
print(f'Looking for tweets matching: {tag}')

def send_tweet() -> int:
    """Send tweet with message and return ID"""
    tweet = api.update_status(message_factory.message())
    print(f'Sent tweet with id {id}')
    return tweet.id

# Stream object to reply to mentions
class Replier(tweepy.Stream):
    def on_status(self, status):
        # Stream found status
        if status.in_reply_to_status_id is not None and status.in_reply_to_user_id == USER_ID:
            if status.text.count(tag) == 1:
                # Don't reply unless explicit mention
                return
        
        print(f'Replying to {status.id} ({status.user.screen_name})')
        api.update_status(f'@{status.user.screen_name} {message_factory.message()}', in_reply_to_status_id=status.id)

replier = Replier(keys['api-key'], keys['api-secret-key'], keys['access-token'], keys['access-token-secret'])
replier_thread = replier.filter(track=[tag], threaded=True)


def run():
    schedule.clear()
    # Schedule tweets
    schedule.every().hour.at(':00').do(send_tweet)

    while True:
        schedule.run_pending()
        sleep(30)

if __name__ == '__main__':
    run()