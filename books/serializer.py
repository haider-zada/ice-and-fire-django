from rest_framework import serializers
from .models import Country, Author, Books


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


class CreateCountrySerializer(serializers.ModelSerializer):
    """
        Serializer for country creation without name user can not create country to field required set to true
    """
    name = serializers.CharField(required=True)

    class Meta:
        model = Country
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    """
        serializer for get and update country
    """
    name = serializers.CharField(required=False)

    class Meta:
        model = Country
        fields = ['name']


class CreateAuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Author
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    isbn = serializers.CharField(required=False)
    authors = AuthorSerializer(required=False, many=True)
    number_of_pages = serializers.IntegerField(required=False, min_value=1)
    publisher = serializers.CharField(required=False)
    country = serializers.SerializerMethodField('get_country_name', required=False)
    release_date = serializers.DateField(required=False)

    def get_country_name(self, obj):
        return obj.country.name

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

    def create(self, validated_data):

        authors = validated_data.pop('authors')
        country_id = validated_data.pop('country')
        """
            Checking if country instance provided by user exists or not
        """
        try:
            country_instance = Country.objects.get(id=country_id)
        except Country.DoesNotExist:
            raise serializers.ValidationError(detail="country does not exist", code=404)

        """Book instance creation"""
        book = Books.objects.create(country_id=country_id, **validated_data)

        for name in authors:
            """
                These lines of code will create author if it does not exist and return newly created author else
                it will return the existing author instance.
            """
            author, created = Author.objects.get_or_create(name=name)
            book.authors.add(author.id)

        return book

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
