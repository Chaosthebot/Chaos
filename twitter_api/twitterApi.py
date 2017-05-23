#!/usr/bin/env python

import twitter
import json

class Twitter:

    def __init__(self):
        with open('/etc/twitter.json') as data_file:
            data = json.load(data_file)
        encoding = None
        self.api = twitter.Api(consumer_key=data["consumer_key"], consumer_secret=data["consumer_secret"],
                      access_token_key=data["access_key"], access_token_secret=data["access_secret"],
                      input_encoding=encoding)

    def postTweet(self,message):
        try:
            status = self.api.PostUpdate(message)
        except:
            #TODO clean message and add more exception
            print 'twitter fail because message too long or encoding problem'