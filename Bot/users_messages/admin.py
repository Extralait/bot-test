from django.contrib import admin

from telegram.models import TelegramUser
from users_messages.models import Dialog

admin.site.register(TelegramUser)
admin.site.register(Dialog)

