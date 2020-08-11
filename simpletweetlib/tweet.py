# coding: utf-8
"""Tweet Client"""
from ._auth import get_auth_session


class Tweet:
    """
    t = Tweet(consumer_key, consumer_secret, access_token, access_token_secret)
    t.tweet('test tweet by twitter api')
    """

    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 access_token,
                 access_token_secret):
        self.twitter = get_auth_session(consumer_key,
                                        consumer_secret,
                                        access_token,
                                        access_token_secret)

    def tweet(self, msg):
        self.twitter.post(
            "https://api.twitter.com/1.1/statuses/update.json?status={}"
            .format(msg))
