import pytest

from ads.serializers import AdListSerializer


@pytest.mark.django_db
def test_ad_detail(client, ad, access_token):
    response = client.get(f'/ad/{ad.pk}/', HTTP_AUTHORIZATION='Bearer ' + access_token)
    assert response.status_code == 202
    assert dict(response.data) == AdListSerializer(ad).data