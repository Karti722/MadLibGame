from rest_framework import serializers
from .models import MadLib

class MadLibSerializer(serializers.ModelSerializer):
    class Meta:
        model = MadLib
        fields = '__all__'
