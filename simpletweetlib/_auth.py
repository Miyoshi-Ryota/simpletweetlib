# coding: utf-8

from requests_oauthlib import OAuth1Session


def get_auth_session(consumer_key,
                     consumer_secret,
                     access_token,
                     access_token_secret):
    return OAuth1Session(consumer_key,
                         client_secret=consumer_secret,
                         resource_owner_key=access_token,
                         resource_owner_secret=access_token_secret)
