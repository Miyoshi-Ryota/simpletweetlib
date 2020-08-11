# coding: utf-8

import twitterapilib.twitterapilib.auth as auth
import urllib.parse

class Profile:
    """
    p = Profile(consumer_key, consumer_secret, access_token, access_token_secret)
    p.change_name('mrcsce')
    """

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.twitter = auth.get_auth_session(consumer_key,
                                             consumer_secret,
                                             access_token,
                                             access_token_secret)

    def change_name(self, name):
        name = urllib.parse.quote(name)
        self.twitter.post('https://api.twitter.com/1.1/account/update_profile.json?name={}'.format(name))


