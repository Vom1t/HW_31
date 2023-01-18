from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование', unique=True)
    slug = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(0), MaxLengthValidator(10)])
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(
        max_length=50,
        db_index=True,
        verbose_name='Заголовок',
        null=False,
        blank=False,
        validators=[MinLengthValidator(10)]
    )
    author = models.ForeignKey(User, verbose_name='Автор', related_name='ads', on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name='Стоимость',
        validators=[MinValueValidator(0)]
    )
    description = models.CharField(max_length=500 )
    is_published = models.BooleanField(default=False, verbose_name='Состояние')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name
