from django.urls import path

from Config.telegram import WEBHOOK_URL_PATH
from telegram.views import Webhook

urlpatterns = [
    path(f'{WEBHOOK_URL_PATH[1:]}', Webhook.as_view()),
]
