from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from users.validators import CheckBirthDate


class Locations(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=False)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=False)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'


    def __str__(self):
        return self.name

class UserRoles:
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = ((MEMBER, 'Пользователь'),
               (MODERATOR, 'Модератор'),
               (ADMIN, 'Администратор'),)


class User(AbstractUser):

    age = models.PositiveSmallIntegerField(verbose_name='Возраст', null=True, blank=True)
    locations = models.ManyToManyField(Locations)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.MEMBER, max_length=10)
    birth_date = models.DateField(validators=[CheckBirthDate], verbose_name='День рождения')
    email = models.EmailField(
        unique=True, verbose_name='E-mail',
        validators=[RegexValidator(regex='@rambler.ru', inverse_match=True,
                                   message='Запрещена регистрация с почтового адреса в домене rambler.ru.')
                    ]
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
