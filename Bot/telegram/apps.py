from random import random
from time import sleep

from django.apps import AppConfig
from telebot.apihelper import ApiTelegramException


class TelegramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram'

    def ready(self):
        # Set webhook
        from Config.telegram import WEBHOOK_URL_BASE, WEBHOOK_URL_PATH
        from telegram.services.dialogue import bot

        connect =False
        while not connect:
            try:
                bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)
                connect = True
            except ApiTelegramException:
                sleep(random() * 5)


