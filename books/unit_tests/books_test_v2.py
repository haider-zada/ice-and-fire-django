from rest_framework.test import APITestCase
from books.models import Books, Country, Author

# Create your tests here.


class BooksTestCaseV2(APITestCase):

    def setUp(self):
        country_json = {"name": "pakistan"}
        self.country = Country.objects.create(**country_json)

        book_json = {"name": "book alpha", "isbn": "32565454", "country": self.country,
                     "number_of_pages": 125, "publisher": "xyz", "release_date": "2019-12-12"}

        self.book = Books.objects.create(**book_json)
        self.author = Author.objects.create(**{"name": "arbisoft"})
        self.book.authors.add(self.author.id)

    def test_create_book_with_invalid_fields(self):
        """Invalid data 400 will be returned"""

        response = self.client.post('/api/v2/books/', {'code': 'Foo Bar'}, format='json')
        self.assertEqual(400, response.data['status_code'])

    def test_create_book(self):

        book = {"name": "book test", "isbn": "3256545489", "authors": ["lee"], "country": self.country.id,
                "number_of_pages": 125,
                "publisher": "xyz", "release_date": "2019-12-12"}

        response = self.client.post('/api/v2/books/', book, format='json')
        self.assertEqual(201, response.data['status_code'])

    def test_list_books(self):
        response = self.client.get('/api/v2/books/', format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_book_by_id(self):
        response = self.client.get('/api/v2/books/{}/'.format(self.book.id), format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_update_book(self):
        body = {'name': 'abcd'}
        response = self.client.patch('/api/v2/books/{}/'.format(self.book.id), body, format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_delete_book(self):
        response = self.client.delete('/api/v2/books/{}/'.format(self.book.id), format='json')
        self.assertEqual(204, response.data['status_code'])
