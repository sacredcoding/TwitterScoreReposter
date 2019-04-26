import twitteracc
import sportssc

acc = twitteracc.TwitterAcc()
acc.CONSUMER_KEY = ''
acc.CONSUMER_SECRET = ''
acc.ACCESS_TOKEN = ''
acc.ACCESS_TOKEN_SECRET = ''
acc.authenticate()

sport = sportssc.SportsScore('St. Louis Blues', 'hockey')
matches = sport.getSportsMatches()
score = sport.findTargetScore(matches)

acc.updateStatus(score)