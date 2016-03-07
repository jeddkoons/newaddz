import os
import time
from random import random
from twython import Twython, TwythonError

app_key = "0s24wXPrr5Qe6enob5Xyn7VyZ"
app_secret = "jI0JY8RQMv7rylZnzdzIK6bLNcPGiPf8u4d7Fq0oz9PEAIdc92"
oauth_token = "704999209636864000-9kbaJ8hms0BdI0aF2vdA2JE24XXNOiv"
oauth_token_secret = "wjEqiZLI2ieu5b9ydWrNeiWKupJcrWxJ9n8jDYVvoUYpe"


RUN_EVERY_N_SECONDS = 60*30 # e.g. 60*5 = tweets every five minutes



naughty_words = [" -RT"]
good_words = ["%22adderall got me like%22", "%22vyvanse got me like%22", "%22vyvanse had me like%22", "%22adderall had me like%22", "%22TFW vyvanse%22", "%22TFW adderall%22"]
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

search_results = twitter.search(q=keywords, count=10)
try:
    for tweet in search_results["statuses"]:
        try:
            twitter.retweet(id = tweet["id_str"])
        except TwythonError as e:
            print e
           
except TwythonError as e:
    print e
    
  
time.sleep(RUN_EVERY_N_SECONDS)

if __name__ == '__main__':
    main()
