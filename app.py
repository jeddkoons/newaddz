import os
import time
from random import random
from twython import Twython, TwythonError

app_key = "0s24wXPrr5Qe6enob5Xyn7VyZ"
app_secret = "jI0JY8RQMv7rylZnzdzIK6bLNcPGiPf8u4d7Fq0oz9PEAIdc92"
oauth_token = "704999209636864000-9kbaJ8hms0BdI0aF2vdA2JE24XXNOiv"
oauth_token_secret = "wjEqiZLI2ieu5b9ydWrNeiWKupJcrWxJ9n8jDYVvoUYpe"
TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21

RUN_EVERY_N_SECONDS = 60*15 # e.g. 60*5 = tweets every five minutes



naughty_words = [" -RT"]
good_words = ["vyvanse got me like", "adderall got me like", "adderall had me like", "TFW vyvanse"]
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

#The obligatory first status update to test
twitter.update_status(status="Hello world.")

search_results = twitter.search(q=keywords, count=100)
try:
    for tweet in search_results["statuses"]:
        try:
            twitter.retweet(id = tweet["id_str"])
        except TwythonError as e:
            print e
           
except TwythonError as e:
    print e
    
  
        # random_favoriting(['apples', 'oranges'], handle)
time.sleep(RUN_EVERY_N_SECONDS)

if __name__ == '__main__':
    main()
