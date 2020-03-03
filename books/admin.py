from django.contrib import admin
from .models import *

# Register your models here
"""
    Admin sites registration
"""
admin.site.register(Country)
admin.site.register(Author)
admin.site.register(Books)