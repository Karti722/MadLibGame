from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MadLibViewSet

router = DefaultRouter()
router.register(r'madlibs', MadLibViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
