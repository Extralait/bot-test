import json
import pickle
from time import sleep

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from Config.telegram import bot
from telegram.services.tasks import get_state, save_state, get_dialogs, get_dialog
from users_messages.services.state import get_state_machine


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    dialogs = get_dialogs.delay()
    while not dialogs.ready():
        sleep(0.01)
    dialogs = dialogs.get()

    bot.reply_to(message,
                 "Что вас интересует?",
                 reply_markup=gen_dialog_choice_markup(dialogs))


def gen_dialog_choice_markup(dialogs):
    markup = InlineKeyboardMarkup()
    markup.row_width = dialogs.count()
    for dialog in dialogs:
        markup.add(InlineKeyboardButton(dialog.name, callback_data=f'dialog_choice_{dialog.pk}'))
    return markup


def gen_markup(step):
    markup = InlineKeyboardMarkup()
    choices = step.get("choices")
    if choices:
        markup.row_width = len(choices)
        for choice in choices:
            markup.add(InlineKeyboardButton(choice['message'], callback_data=choice['trigger']))
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    external_id = call.from_user.id,
    first_name = call.from_user.first_name,
    last_name = call.from_user.last_name,
    username = call.from_user.username,
    state = get_state.delay(external_id[0],
                            first_name[0],
                            username[0],
                            last_name[0])
    while not state.ready():
        sleep(0.01)
    state = state.get()
    if call.data.startswith('dialog_choice_'):
        dialog = get_dialog.delay(call.data.replace('dialog_choice_', ''))
        while not dialog.ready():
            sleep(0.01)
        dialog = dialog.get()
        state = pickle.loads(get_state_machine(json.loads(dialog.state_config)))

    print(state)
    state_dict = state.state_dict
    print(state_dict)
    step = state_dict[state.state]
    print(step)
    if call.data.startswith('dialog_choice_'):
        save_state.delay(external_id, pickle.dumps(state))
        bot.send_message(call.from_user.id,
                         step["message_template"].format(*state.answers),
                         reply_markup=gen_markup(step))
    else:
        if step.get("choices"):
            state.answers[step["pk"]] = sorted(step["choices"], key=lambda x: x["trigger"] == call.data)[-1]["message"]
        print(state.answers)
        getattr(state, call.data)()
        step = state_dict[state.state]
        print(state)
        save_state.delay(external_id, pickle.dumps(state))

        bot.send_message(call.from_user.id,
                         step["message_template"].format(*state.answers),
                         reply_markup=gen_markup(step))
