from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Books

# Create your tests here.


class BooksTestCase(APITestCase):

    def setUp(self):
        book = {"name": "book alpha", "isbn": "32565454", "authors": ["a", "b"], "country": "pakistan",
                "number_of_pages": 125, "publisher": "xyz", "release_date": "2019-12-12"}

        self.book = Books.objects.create(**book)

    def test_1(self):
        """Invalid data 400 will be returned"""

        response = self.client.post('/api/v1/books/', {'code': 'Foo Bar'}, format='json')
        self.assertEqual(400, response.data['status_code'])

    def test_2(self):
        body = {"name": "book test", "isbn": "32565454", "authors": ["a", "b"], "country": "pakistan",
                "number_of_pages": 125,
                "publisher": "xyz", "release_date": "2019-12-12"}

        response = self.client.post('/api/v1/books/', body, format='json')
        self.assertEqual(201, response.data['status_code'])

    def test_3(self):
        response = self.client.get('/api/v1/books/', format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_4(self):
        body = {'name': 'book test'}

        response = self.client.post('/api/v1/books/filter/', body, format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_5(self):
        body = {'name': 'book test', 'year': 2019}

        response = self.client.post('/api/v1/books/filter/', body, format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_6(self):
        response = self.client.get('/api/v1/books/12345/', format='json')
        self.assertEqual(404, response.data['status_code'])

    def test_7(self):
        response = self.client.get('/api/v1/books/{}/'.format(self.book.id), format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_8(self):
        response = self.client.patch('/api/v1/books/{}/'.format(self.book.id), {'name': 'abcd'}, format='json')
        self.assertEqual(200, response.data['status_code'])
