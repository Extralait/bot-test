import logging
from random import random
from time import sleep

import telebot
from telebot.apihelper import ApiTelegramException

from Config.settings import TELEGRAM_TOKEN, WEBHOOK_HOST, WEBHOOK_PORT, WEBHOOK_LISTEN, WEBHOOK_SSL_CERT, \
    WEBHOOK_SSL_PRIV

# Quick'n'dirty SSL certificate generation:
#
# openssl genrsa -out webhook_pkey.pem 2048
# openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
#
# When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
# with the same value in you put in WEBHOOK_HOST

WEBHOOK_URL_BASE = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}/telegram"
WEBHOOK_URL_PATH = f"/{TELEGRAM_TOKEN}/"

logger = telebot.logger

telebot.logger.setLevel(logging.INFO)

connect = False

while not connect:
    try:
        bot = telebot.TeleBot(TELEGRAM_TOKEN)
        connect = True
    except ApiTelegramException:
        sleep(random()*5)

# bot.remove_webhook()

