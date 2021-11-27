import json

from django.core.management import BaseCommand

from Config import settings
from users.models import User
from users_messages.models import Dialog


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Dialog.objects.count() == 0:
            Dialog.objects.update_or_create(
                pk=1,
                name="Заказ пиццы",
                state_config=json.dumps([
                    {
                        "state": "pizza_choice",
                        "message_template": "Какую вы хотите пиццу?",
                        "choices": [
                            {
                                "trigger": "big",
                                "message": "Большую",
                                "dest": "pay_type_choice"
                            },
                            {
                                "trigger": "small",
                                "message": "Маленькую",
                                "dest": "pay_type_choice"
                            },
                        ],
                    },
                    {
                        "state": "pay_type_choice",
                        "message_template": "Как вы будете платить?",
                        "choices": [
                            {
                                "trigger": "cash",
                                "message": "Наличными",
                                "dest": "confirm"
                            },
                            {
                                "trigger": "card",
                                "message": "Картой",
                                "dest": "confirm"
                            },
                            {
                                "trigger": "back",
                                "message": "Назад",
                                "dest": "pizza_choice"
                            }
                        ],
                    },
                    {
                        "state": "confirm",
                        "message_template": "Вы хотите {0} пиццу, оплата - {1}?",
                        "choices": [
                            {
                                "trigger": "yes",
                                "message": "Да",
                                "dest": "end"
                            },
                            {
                                "trigger": "back",
                                "message": "Назад",
                                "dest": "pay_type_choice"
                            }
                        ],
                        "dest": "pay_type_choice"
                    },
                    {
                        "state": "end",
                        "previous": "confirm",
                        "message_template": "Спасибо за заказ"
                    }
                ],
                    ensure_ascii=False,
                    indent=4)
            )
