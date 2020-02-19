from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    number_of_pages = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=250, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    authors = ArrayField(
        models.CharField(max_length=150, null=True, blank=True),
        default=list,
        null=True
    )
