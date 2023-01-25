import pytest


@pytest.mark.django_db
def test_ad_create(client, category, access_token):
    data = {
        'name': 'Test Ad Pytest',
        'category': [str(category.pk)],
        'price': 12000
    }

    expected_data = {
        'id': 1,
        'name': 'Test Ad Pytest',
        'author': 'test',
        'price': '12000',
        'description': None,
        'is_published': False,
        'image': None,
        'category': [str(category.pk)],
    }

    response = client.post('/ad/create/', data, content_type='application/json',
                           HTTP_AUTHORIZATION='Bearer ' + access_token)
    assert response.status_code == 201
    assert response.data == expected_data
