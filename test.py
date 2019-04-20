import tweepy

CONSUMER_KEY = "wvLGq7PCgcob1oB60sxDCQ4FU"
CONSUMER_SECRET = "kXmbt5ZTC6L1H8gvMit8sX0DDu4TC2BdjlhyT6LeFuFzTYx8TE"
ACCESS_KEY = "1113827435701768193-QG3CqW9WzqjGrOYaRsmxZYwJHp28e7"
ACCESS_SECRET = "M2KohbIaSJwiK2q3BHbUPRDk599N4GS6Y50MwjxMSCzyY"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
api.update_status('Updating using OAuth authentication via Tweepy!')
