from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import Utils, create_response
from common.constants import *
from .serializer import *
from rest_framework import viewsets

# Create your views here.

util_obj = Utils()


class ExternalBook(APIView):

    def get(self, request):

        book_name = request.GET.get('name')
        result = util_obj.get_icefire_data(book_name=book_name)
        return Response(result)


class BookView(APIView):

    def get(self, request, id=None):

        if id is None:

            entity = Books.objects.all()
            serializer_obj = BookSerializer(entity, many=True)

        else:
            try:

                entity = Books.objects.get(id=id)
                serializer_obj = BookSerializer(entity)

            except Books.DoesNotExist:
                return Response(create_response(status_code=404, status=ENTITY_NOT_FOUND, data=[]))

        return Response(create_response(status_code=200, status=MESSAGE_SUCCESS, data=serializer_obj.data))

    def post(self, request):

        serializer_obj = CreateBookSerializer(data=request.data)

        if serializer_obj.is_valid():
            
            serializer_obj.save()
            return Response(create_response(status_code=201, status=MESSAGE_SUCCESS, data=[serializer_obj.validated_data]))

        return Response(create_response(status_code=400, status=INVALID_MISSING_FIELDS, data=[]))

    def patch(self, request, id=None):

        try:
            
            entity = Books.objects.get(id=id)
            status = 'The book {} was updated successfully'.format(entity.name)
            serializer_obj = BookSerializer(entity, data=request.data)

            if serializer_obj.is_valid():
                updated_book = serializer_obj.save()
                data = BookSerializer(updated_book).data

                return Response(create_response(status_code=200, status=status, data=data))

            return Response(create_response(status_code=400, status=INVALID_MISSING_FIELDS, data=[]))

        except Books.DoesNotExist:
            return Response(create_response(status_code=404, status=ENTITY_NOT_FOUND, data=[]))

    def delete(self, request, id=None):

        try:
            
            entity = Books.objects.get(id=id)
            status = 'The book {} was deleted successfully'.format(entity.name)
            entity.delete()

            return Response(create_response(status_code=204, status=status, data=[]))

        except Books.DoesNotExist:
            return Response(create_response(status_code=404, status=ENTITY_NOT_FOUND, data=[]))


class BookFilterView(APIView):
    """
        User can filter on books using year, name, publisher and country.
    """
    def post(self, request):

        serializer_obj = BookFilterSerializer(data=request.data)

        if serializer_obj.is_valid():
            year = serializer_obj.validated_data.pop('year', None)

            if year:
                book = Books.objects.filter(**serializer_obj.validated_data, release_date__year=year)

            else:
                book = Books.objects.filter(**serializer_obj.validated_data)

            data = BookSerializer(book, many=True).data
            return Response(create_response(status_code=200, status=MESSAGE_SUCCESS, data=data))

        return Response(create_response(status_code=400, status=INVALID_MISSING_FIELDS, data=[]))


class BookViewSet(viewsets.ModelViewSet):
    """
        View-Set for books CRUD
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        response = super(BookViewSet, self).list(request, *args, **kwargs)
        response.data = create_response(status_code=200, status=MESSAGE_SUCCESS, data=response.data)
        return response

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            entity = Books.objects.get(pk=pk)
            serializer = BookSerializer(entity)
            return Response(create_response(status_code=200, status=MESSAGE_SUCCESS, data=serializer.data))

        except Books.DoesNotExist:
            return Response(create_response(status_code=404, status=ENTITY_NOT_FOUND, data=[]))

    def create(self, request, *args, **kwargs):

        serializer_obj = CreateBookSerializer(data=request.data)

        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(create_response(status_code=201, status=MESSAGE_SUCCESS, data=[serializer_obj.validated_data]))

        return Response(create_response(status_code=400, status=INVALID_MISSING_FIELDS, data=[]))

    def update(self, request, pk=None, *args, **kwargs):
        try:

            entity = Books.objects.get(pk=pk)
            status = 'The book {} was updated successfully'.format(entity.name)
            serializer_obj = BookSerializer(entity, data=request.data)

            if serializer_obj.is_valid():
                updated_book = serializer_obj.save()
                data = BookSerializer(updated_book).data

                return Response(create_response(status_code=200, status=status, data=data))

        except Books.DoesNotExist:
            return Response(create_response(status_code=404, status=ENTITY_NOT_FOUND, data=[]))

    def destroy(self, request, pk=None, *args, **kwargs):
        try:

            entity = Books.objects.get(pk=pk)
            status = 'The book {} was deleted successfully'.format(entity.name)
            entity.delete()

            return Response(create_response(status_code=204, status=status, data=[]))

        except Books.DoesNotExist:
            return Response(create_response(status_code=404, status=ENTITY_NOT_FOUND, data=[]))


class CountryViewSet(viewsets.ModelViewSet):
    """
        Views-Set for country CRUD
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self, request, *args, **kwargs):
        response = super(CountryViewSet, self).list(request, *args, **kwargs)
        response.data = create_response(status_code=200, status=MESSAGE_SUCCESS, data=response.data)
        return response

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            entity = Country.objects.get(pk=pk)
            serializer = CountrySerializer(entity)
            return Response(create_response(status_code=200, status=MESSAGE_SUCCESS, data=serializer.data))

        except Country.DoesNotExist:
            return Response(create_response(status_code=404, status=ENTITY_NOT_FOUND, data=[]))

    def create(self, request, *args, **kwargs):

        serializer_obj = CreateCountrySerializer(data=request.data)

        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(create_response(status_code=201, status=MESSAGE_SUCCESS, data=[serializer_obj.validated_data]))

        return Response(create_response(status_code=400, status=INVALID_MISSING_FIELDS, data=[]))

    def update(self, request, pk=None, *args, **kwargs):
        try:

            entity = Country.objects.get(pk=pk)
            status = 'The country {} was updated successfully'.format(entity.name)
            serializer_obj = CountrySerializer(entity, data=request.data)

            if serializer_obj.is_valid():
                updated_country = serializer_obj.save()
                data = CountrySerializer(updated_country).data

                return Response(create_response(status_code=200, status=status, data=data))

        except Country.DoesNotExist:
            return Response(create_response(status_code=404, status=ENTITY_NOT_FOUND, data=[]))

    def destroy(self, request, pk=None, *args, **kwargs):
        try:

            entity = Country.objects.get(pk=pk)
            status = 'The country {} was deleted successfully'.format(entity.name)
            entity.delete()

            return Response(create_response(status_code=204, status=status, data=[]))

        except Country.DoesNotExist:
            return Response(create_response(status_code=404, status=ENTITY_NOT_FOUND, data=[]))
