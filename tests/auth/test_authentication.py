import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestAuthenticationEndpoints:

    def test_token_obtain_pair(self, api_client, create_user):
        user = create_user(username='user1', password='pass123')
        url = reverse('token_obtain_pair')
        response = api_client.post(url, {'username': 'user1', 'password': 'pass123'}, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_token_refresh(self, api_client, create_user):
        user = create_user(username='user2', password='pass123')
        url = reverse('token_obtain_pair')
        response = api_client.post(url, {'username': 'user2', 'password': 'pass123'}, format='json')
        refresh_token = response.data['refresh']

        refresh_url = reverse('token_refresh')
        response = api_client.post(refresh_url, {'refresh': refresh_token}, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
