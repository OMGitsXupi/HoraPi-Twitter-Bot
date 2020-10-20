# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = "2kq5mIEwTSmGKf1qci3AImNH3"
    consumer_secret = "Mw4K01o5sAxcrOcA6miYcvkgirNbSww3tpaUXHLRC32eEErGvz"
    access_token = "1181130761333886977-ALyZpmW9iwNJUhxd8HDllPmgBUEZPV"
    access_token_secret = "xhkrTAPWBPKG5a0URHurheuDLUmjL4naQrNtZjipiOxfu"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
