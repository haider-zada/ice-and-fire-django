from rest_framework import serializers
from .models import Books


class IceFireDataSerializer(serializers.Serializer):

    name = serializers.CharField()
    isbn = serializers.CharField()
    authors = serializers.ListField()
    number_of_pages = serializers.IntegerField(source='numberOfPages')
    publisher = serializers.CharField()
    country = serializers.CharField()
    release_date = serializers.SerializerMethodField('get_release_date')

    def get_release_date(self, obj):
        return obj.get('released').split('T')[0]


class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    isbn = serializers.CharField(required=False)
    authors = serializers.ListField(required=False)
    number_of_pages = serializers.IntegerField(required=False, min_value=1)
    publisher = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    release_date = serializers.DateField(required=False)

    class Meta:
        model = Books
        fields = '__all__'


class CreateBookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    isbn = serializers.CharField(required=True)
    authors = serializers.ListField(required=True)
    number_of_pages = serializers.IntegerField(required=True, min_value=1)
    publisher = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    release_date = serializers.DateField(required=True)

    class Meta:
        model = Books
        fields = '__all__'


class BookFilterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    publisher = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    year = serializers.IntegerField(required=False)

    class Meta:
        model = Books
        fields = ['name', 'publisher', 'country', 'year']
