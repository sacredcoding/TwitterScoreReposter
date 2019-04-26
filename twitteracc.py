import tweepy

class TwitterAcc:
    def __init__(self):
        self.CONSUMER_KEY = ''
        self.CONSUMER_SECRET = ''
        self.ACCESS_TOKEN = ''
        self.ACCESS_TOKEN_SECRET = ''
        self.api = ''

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)

        self.api = tweepy.API(auth)

    def updateStatus(self, message):
        self.api.update_status(message)