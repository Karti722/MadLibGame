# serializers.py
from rest_framework import serializers

class MadlibSerializer(serializers.Serializer):
    noun = serializers.CharField(required=True)
    verb = serializers.CharField(required=True)
    adjective = serializers.CharField(required=True)
    adverb = serializers.CharField(required=True)
