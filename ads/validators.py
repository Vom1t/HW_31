from rest_framework import serializers


def check_published(value):
    if value:
        raise serializers.ValidationError(f'Поле is_published при создании объявления не может быть True.')