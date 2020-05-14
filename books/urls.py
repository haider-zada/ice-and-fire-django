"""iceandfire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books import views


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'country', views.CountryViewSet)

"""
    1. external-books api will get data from ice and fire api
    2. urls with v1 is using API VIEWS
    3. urls with v2 is using VIEW SET
"""

urlpatterns = [
    path('external-books', views.ExternalBook.as_view()),

    path('v1/books/', views.BookView.as_view()),
    path('v1/books/<int:id>/', views.BookView.as_view()),
    path('v1/books/filter/', views.BookFilterView.as_view()),

    path('v2/', include(router.urls)),



]
