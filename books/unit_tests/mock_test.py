import unittest
from unittest.mock import patch
from  books.utils import Utils
import json

class MockTestIceAndFire(unittest.TestCase):

    def test_data(self):
        fake_data = self.json_loads()
        with patch('books.utils.requests.get') as mock_obj:
            mock_obj.return_value.status_code = 200
            mock_obj.return_value.text = fake_data

            response = Utils().get_icefire_data()
            self.assertEqual(200, response['status_code'])

    def json_loads(self):
        fake_data = [
            {
                "url": "https://www.anapioficeandfire.com/api/books/1",
                "name": "A Game of Thrones",
                "isbn": "978-0553103540",
                "authors": [
                    "George R. R. Martin"
                ],
                "numberOfPages": 694,
                "publisher": "Bantam Books",
                "country": "United States",
                "mediaType": "Hardcover",
                "released": "1996-08-01T00:00:00",
                "characters": [
                    "https://www.anapioficeandfire.com/api/characters/2",
                    "https://www.anapioficeandfire.com/api/characters/12",
                    "https://www.anapioficeandfire.com/api/characters/13",
                ],
                "povCharacters": [
                    "https://www.anapioficeandfire.com/api/characters/148",
                    "https://www.anapioficeandfire.com/api/characters/208",
                    "https://www.anapioficeandfire.com/api/characters/232",
                    "https://www.anapioficeandfire.com/api/characters/339",
                    "https://www.anapioficeandfire.com/api/characters/583",
                    "https://www.anapioficeandfire.com/api/characters/957",
                    "https://www.anapioficeandfire.com/api/characters/1052",
                    "https://www.anapioficeandfire.com/api/characters/1109",
                    "https://www.anapioficeandfire.com/api/characters/1303"
                ]
            }
        ]
        return json.dumps(fake_data)