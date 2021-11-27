# This example show how to use inline keyboards and process button presses
import telebot

from threading import Thread
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = '2134765598:AAEDsL2EuDD0ZqBCvf9SNUrdkbv9MOhOYn0'

bot = telebot.TeleBot(TELEGRAM_TOKEN)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup

bot.remove_webhook()

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    external_id = call.from_user.id,
    first_name = call.from_user.first_name,
    last_name = call.from_user.last_name,
    username = call.from_user.username,
    print((external_id,first_name,last_name,username))
    if call.data == "cb_yes":
        bot.send_message(call.from_user.id, "Yes/no?", reply_markup=gen_markup())
    elif call.data == "cb_no":
        bot.send_message(call.from_user.id, "Yes/no?", reply_markup=gen_markup())


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())


bot.infinity_polling()
# Thread(target=bot.infinity_polling, args=(True,)).start()
