from twitter import *
from Toxicity import Model
import numpy as np
import os, ssl
import json


class TwitterDataHandler:
    def __init__(self):
        dummy = 1

    def getTweetsFromUser(self,username):
        '''takes in username and returns a dictionary consisting of all tweets received from the twitter api'''
        print(username)
        if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
                getattr(ssl, '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context

        consumer_key, consumer_secret, token, token_secret = self.getTwitterKeys()
        t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

        resp = t.statuses.user_timeline(screen_name=username)
        tweet_dict = self.getTweetsList(resp)
        score = self.scoreTweets(tweet_dict)
        tweet_dict['score'] = (str(score))
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
            tweet_text[i] = t.get('text', '')
        return tweet_text

    def scoreTweets(self,tweets):
        model = Model()
        return np.mean([model.score(k) for k, v in tweets.items()])

    def scoreUser(self,username):
        return self.getTweetsFromUser(username)