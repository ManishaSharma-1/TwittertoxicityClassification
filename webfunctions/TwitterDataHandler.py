from twitter import *
from Toxicity import Model
import numpy as np
import os, ssl
import json


class TwitterDataHandler:
    def __init__(self,model):
        self.model = model
    
    def getTweetsFromUser(self,username):
        '''takes in username and returns a dictionary consisting of all tweets received from the twitter api'''
        print(username)
        if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
                getattr(ssl, '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context

        consumer_key, consumer_secret, token, token_secret = self.getTwitterKeys()
        t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

        resp = t.statuses.user_timeline(screen_name=username)
        print(resp)
        tweet_dict = self.getTweetsList(resp)
        score = self.scoreTweets(tweet_dict)
        tweet_dict['score'] = (str(score))
        tweet_dict['username'] = username
        return  tweet_dict

    def getTwitterKeys(self):
        with open("./webfunctions/twitter_api.template.json") as keyFile:
            keys = json.load(keyFile)

        consumer_key = keys['consumer_key']
        consumer_secret = keys['consumer_secret']
        token = keys['token']
        token_secret = keys['token_secret']

        return consumer_key, consumer_secret, token, token_secret

    def getTweetsList(self,resp):
        tweet_text = dict()
        for i, t in enumerate(resp):
            tweet = t.get('text', '')
            strs = tweet.split(' ',1)
            if strs[0] == 'RT':
            #     retweets ignore
                continue
            elif strs[0][0]=='@':
                continue
            tweet_text[i] = t.get('text', '')
            # if len(tweet_text) == 10:
            #     break
        return tweet_text

    def scoreTweets(self,tweets):
        scores = [self.model.score(str(v)) for k, v in tweets.items()]
        print(scores)
        return np.mean(scores)

    def scoreUser(self,username):
        return self.getTweetsFromUser(username)