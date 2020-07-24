import tweepy
import time

auth = tweepy.OAuthHandler("dZI1PLdwwihr5gQiMTBxXnXhm","gJt3UZ4Xo2tW1kNsBHrLY5PAgKsJXnHVwFvftAIac48QjntxZL")
auth.set_access_token("1253064171899494406-evCmLy9HcvVlt5cWHGCfIUMLzHKCSU","mlnrUNvFbEVlYarjH7btdd45Lo3KMiakCsulyzTzHC8E2")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = "#harrystyles"
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print("Tweet Liked")
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break