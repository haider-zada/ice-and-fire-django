from rest_framework.test import APITestCase


class BooksTestCase(APITestCase):

    def test_ice_and_fire_external(self):
        """
            This test case will fetch data from external API using name provided in Query Param

        """
        response = self.client.get('/api/external-books?name=A Game of Thrones', format='json')
        self.assertEqual(200, response.data['status_code'])

    def test_ice_and_fire_external_invalid_search(self):
        """
            This test case will fetch data from external API using name provided in Query Param length will be equal to
            zero as providing invalid name

        """
        response = self.client.get('/api/external-books?name=abc23123', format='json')
        self.assertEqual(200, response.data['status_code'])
        self.assertEqual(0, len(response.data['data']))
