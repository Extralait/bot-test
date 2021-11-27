from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import telebot
from Config.telegram import bot


class Webhook(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        json_string = request.data
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return Response(status=status.HTTP_200_OK)

