from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class APITests(TestCase):
    def test_vowel_count(self):
        url = reverse('vowel-count')  # Usando o nome da URL 'vowel-count'
        data = {'words': ['batman', 'robin', 'coringa']}
        response = self.client.post(
            url, data, format='json', content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, {'batman': 2, 'robin': 2, 'coringa': 3}
        )

    def test_sort_asc(self):
        url = reverse('sort-words')  # Usando o nome da URL 'sort-words'
        data = {'words': ['batman', 'robin', 'coringa'], 'order': 'asc'}
        response = self.client.post(
            url, data, format='json', content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ['batman', 'coringa', 'robin'])

    def test_sort_desc(self):
        url = reverse('sort-words')  # Usando o nome da URL 'sort-words'
        data = {'words': ['batman', 'robin', 'coringa'], 'order': 'desc'}
        response = self.client.post(
            url, data, format='json', content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ['robin', 'coringa', 'batman'])
