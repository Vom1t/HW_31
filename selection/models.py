
from django.db import models

from ads.models import Ad
from users.models import User


class Selection(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', related_name='owner')
    items = models.ManyToManyField(Ad, verbose_name='Объявления')

    class Meta:
        unique_together = ('name', 'owner')
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name
