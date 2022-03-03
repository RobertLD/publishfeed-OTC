import tweepy

class Twitter:

    def __init__(self, consumer_key, consumer_secret, access_key,access_secret,bearer_token):
        
        client = tweepy.Client(bearer_token = bearer_token,
        consumer_key = consumer_key,consumer_secret = consumer_secret,access_token = access_key,access_token_secret = access_secret)
        self.api = client


    def update_status(self, text):
        return self.api.create_tweet(text=text, user_auth = True)

