import tweepy
import json
import logging
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import csv
import os
from dotenv import load_dotenv
load_dotenv()

class TweetsListener(tweepy.StreamListener):

    def on_connect(self):
        print ("Estoy conectado")

    def on_status(self, status):
        if status.user.id_str != '235200726':
            return
        if hasattr(status, "retweeted_status"):
            return
        else:
            try:
                print(status.extended_tweet["full_text"])
                tweet = (status.extended_tweet["full_text"])
            except AttributeError:
                print(status.text)
                tweet = (status.text)
                
        api.update_status(tweet)
        
    def on_error(self, status_code):
        print ("Error", status_code)

consumer_key = os.getenv('pwconsumer_key')
consumer_secret = os.getenv('pwconsumer_secret')
access_token = os.getenv('pwaccess_token')
access_token_secret = os.getenv('pwaccess_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

stream = TweetsListener()
streamingApi = tweepy.Stream(auth=api.auth, listener=stream)

streamingApi.filter(
    follow=["235200726"]
)
