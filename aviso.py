
import tweepy
import logging
from config import create_api
from datetime import date
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def aviso(api):
    tweet = api.update_status(status='Son las 3:14 del ' + date.today().strftime("%d/%m/%y"))
    logger.info("aviso puesto: " + tweet.created_at.strftime("%H:%M:%S"))

def main():
    api = create_api()
    aviso(api)

if __name__ == "__main__":
    main()
