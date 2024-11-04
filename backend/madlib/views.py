from rest_framework import viewsets
from .models import MadLib
from .serializers import MadLibSerializer

class MadLibViewSet(viewsets.ModelViewSet):
    queryset = MadLib.objects.all()
    serializer_class = MadLibSerializer
