#! /usr/bin/env python3

import tweepy
import auth_keys


def authenticate():
    """Handles authentication with Twitter API"""
    auth = tweepy.OAuthHandler(auth_keys.consumer_key, auth_key.consumer_secret)
    auth.set_access_token(auth_keys.access_token, auth_keys.access_token_secret)
    api = tweepy.API(auth)
    return api

#def get_user():
#    """Gets the user and returns user object"""
#    handle = input("Enter Twitter handle of user you wish to analyze: ")

if __name__ == "__main__":
    api = authenticate()
    