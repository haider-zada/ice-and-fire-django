from rest_framework.test import APITestCase
from books.models import Country

# Create your tests here.


class BooksTestCase(APITestCase):

    def setUp(self):
        country = {"name": "pakistan"}

        self.country = Country.objects.create(**country)

    def test_create_country_with_invalid_data(self):
        """As passing invalid data to serializer so serializer validation will fail and 400 will be returned"""

        response = self.client.post('/api/v2/country/', {'code': 'Foo Bar'}, format='json')
        self.assertEqual(400, response.data['status_code'])

    def test_create_country(self):
        """
            Country Creation
        """
        body = {"name": "pakistan"}

        response = self.client.post('/api/v2/country/', body, format='json')
        self.assertEqual(201, response.data['status_code'])

    def test_list_countries(self):
        response = self.client.get('/api/v2/country/', format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_country_by_id(self):
        response = self.client.get('/api/v2/country/{}/'.format(self.country.id), format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_update_country(self):
        body = {'name': 'pak'}

        response = self.client.patch('/api/v2/country/{}/'.format(self.country.id), body, format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_delete_country(self):
        response = self.client.delete('/api/v2/country/{}/'.format(self.country.id), format='json')
        self.assertEqual(204, response.data['status_code'])

    def test_get_country_by_invalid_id(self):
        """providing invalid id country does not exist returned"""

        response = self.client.get('/api/v2/country/12345/', format='json')
        self.assertEqual(404, response.data['status_code'])