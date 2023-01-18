
from datetime import datetime

import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = 'test'
    password = 'password'
    birth_date = datetime.strptime('2000-01-01', '%Y-%m-%d')
    email = 'test@example.com'
    django_user_model.objects.create_user(username=username, password=password,
                                          role='admin', birth_date=birth_date, email=email)

    response = client.post('/user/token/',
                           {'username': username, 'password': password},
                           content_type='application/json')
    return response.data['access']