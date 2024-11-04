# project_name/urls.py

from django.contrib import admin
from django.urls import path, include  # include is necessary to reference app urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('madlib.urls')),  
]
