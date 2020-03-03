from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = 'location_country'


class Author(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = 'authors'


class Books(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    country = models.ForeignKey(Country, related_name='book_country_fk', on_delete=models.CASCADE)
    number_of_pages = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=250, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='book_author_fk')

    class Meta:
        db_table = 'books'