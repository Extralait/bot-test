from transitions import Machine

from Config.celery import app as celery_app
from Config.telegram import bot
from telegram.models import TelegramUser
from users_messages.models import Dialog
from users_messages.services.state import get_state_machine
import pickle


@celery_app.task(queue='solo_task', routing_key='solo_task')
def get_state(external_id,
              first_name,
              last_name,
              username,
              state_config=None) -> Machine or None:
    """
    Получить экземпляр User
    """
    try:
        user = TelegramUser.objects.get(external_id=external_id)
    except TelegramUser.DoesNotExist:
        user = TelegramUser.objects.create(
            external_id=external_id,
            first_name=first_name,
            last_name=last_name[0],
            username=username[0],
            state=get_state_machine(state_config)
        )
    if user.state:
        return pickle.loads(user.state)
    else:
        return None


@celery_app.task(queue='solo_task', routing_key='solo_task')
def save_state(external_id, state):
    user = TelegramUser.objects.get(external_id=external_id[0])
    user.state = state
    user.save()


@celery_app.task(queue='solo_task', routing_key='solo_task')
def get_dialogs():
    return Dialog.objects.all()


@celery_app.task(queue='solo_task', routing_key='solo_task')
def get_dialog(pk):
    return Dialog.objects.get(pk=pk)
