#!/usr/bin/env python

import twitter

class Twitter:

    def __init__(self):
        consumer_key = "WXfZoJi7i8TFmrGOK5Y7dVHon"
        consumer_secret = "EE46ezCkgKwy8GaKOFFCuMMoZbwDprnEXjhVMn7vI7cYaTbdcA"
        access_key = "867082422885785600-AJ0LdE8vc8uMs21VDv2jrkwkQg9PClG"
        access_secret = "qor8vV5kGqQ7mJDeW83uKUk2E8MUGqp5biTTswoN4YEt6"
        encoding = None
        self.api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_token_key=access_key, access_token_secret=access_secret,
                      input_encoding=encoding)

    def postTweet(self,message):
        try:
            status = self.api.PostUpdate(message)
        except:
            print 'fuckedup'