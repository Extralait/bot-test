from django.db import models


class Dialog(models.Model):
    name = models.CharField('Name', max_length=100)
    state_config = models.JSONField('State config')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Dialog"
        verbose_name_plural = "Dialogs"

