from django.db import models


class TelegramUser(models.Model):
    external_id = models.PositiveBigIntegerField("External ID", primary_key=True)
    first_name = models.CharField("First name", max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    username = models.CharField("Username", max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    state = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return f'{self.external_id} - {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Telegram user"
        verbose_name_plural = "Telegram users"

