import tweepy
from config import create_api
import json
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('favs-log')

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        logger.info("Api created")

    def on_status(self, tweet):
        try:
            if tweet.user.id == self.me.id:
                return
            if tweet.created_at.hour==1 and tweet.created_at.minute==14 and not tweet.favorited:
                try:
                    tweet.favorite()
                    logger.info("Dado fav a: "+str(tweet.id))
                except Exception as e:
                    logger.error("Error en el fav de "+str(tweet.id)+": "+str(e))
            else:
                logger.info("No se ha dado fav a: "+str(tweet.id))
        except BaseException as e:
            logger.error('error on_status, '+str(e))

    def on_error(self, status):
        logger.error('Error')

    def on_timeout(self):
        logger.info('Timeout...')
        return True

    def on_limit(self,status):
        logger.info('Rate Limit Exceeded, Sleep for 5 Mins')
        time.sleep(5 * 60)
        return True

def start_stream(api, listener):
    while True:
        try:
            stream = tweepy.Stream(api.auth, listener)
            stream.filter(track=["Hora pi", "horapi"])
        except Exception as e:
            logger.error('Error de stream: '+str(e))
            continue
        print ("Sleep for 1 second")
        time.sleep(1)

def main():
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    start_stream(api, tweets_listener)

if __name__ == "__main__":
    main()
