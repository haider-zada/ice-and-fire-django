import requests
from iceandfire.settings import BASE_URL
from .serializer import IceFireDataSerializer, CreateBookSerializer
from common.utils import create_response
from common.constants import MESSAGE_SUCCESS, MESSAGE_FAILURE
import json


class Utils:

    def get_icefire_data(self, book_name=None):
        """Base URL is defined in settings"""

        url = BASE_URL

        if book_name is not None:
            url = url+book_name

        request_obj = requests.get(url, headers={'Content-type': 'application/json'})
        json_obj = json.loads(request_obj.text)

        if request_obj.status_code == 200:

            serializer_obj = IceFireDataSerializer(json_obj, many=True)
            return create_response(status_code=request_obj.status_code, status=MESSAGE_SUCCESS, data=serializer_obj.data)

        else:
            return create_response(status_code=request_obj.status_code, status=MESSAGE_FAILURE, data=[])
