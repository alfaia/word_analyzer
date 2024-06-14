import pytest
from django.urls import reverse
from rest_framework import status
from django.test import Client
from pytest_django.asserts import assertJSONEqual


@pytest.mark.django_db
class TestAPITests:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = Client()

    def test_vowel_count(self):
        url = reverse('vowel-count')  # Usando o nome da URL 'vowel-count'
        data = {'words': ['batman', 'robin', 'coringa']}
        response = self.client.post(
            url, data, format='json', content_type='application/json'
        )

        assert response.status_code == status.HTTP_200_OK
        assertJSONEqual(
            response.content, {'batman': 2, 'robin': 2, 'coringa': 3}
        )

    def test_sort_asc(self):
        url = reverse('sort-words')  # Usando o nome da URL 'sort-words'
        data = {'words': ['batman', 'robin', 'coringa'], 'order': 'asc'}
        response = self.client.post(
            url, data, format='json', content_type='application/json'
        )

        assert response.status_code == status.HTTP_200_OK
        assertJSONEqual(response.content, ['batman', 'coringa', 'robin'])

    def test_sort_desc(self):
        url = reverse('sort-words')  # Usando o nome da URL 'sort-words'
        data = {'words': ['batman', 'robin', 'coringa'], 'order': 'desc'}
        response = self.client.post(
            url, data, format='json', content_type='application/json'
        )

        assert response.status_code == status.HTTP_200_OK
        assertJSONEqual(response.content, ['robin', 'coringa', 'batman'])
