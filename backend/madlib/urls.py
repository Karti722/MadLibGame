# urls.py

from django.urls import path
from .views import create_madlib

urlpatterns = [
    path('api/madlib/', create_madlib, name='create_madlib'),
]
