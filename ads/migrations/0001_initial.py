# Generated by Django 4.1.5 on 2023-01-21 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Заголовок')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Стоимость')),
                ('description', models.CharField(max_length=500)),
                ('is_published', models.BooleanField(default=False, verbose_name='Состояние')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Наименование')),
                ('slug', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
