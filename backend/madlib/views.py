# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def create_madlib(request):
    # Extract data from request.data
    noun = request.data.get('noun', '')
    verb = request.data.get('verb', '')
    adjective = request.data.get('adjective', '')
    adverb = request.data.get('adverb', '')

    # Create the completed Mad Lib
    madlib = f"The {adjective} {noun} will {verb} {adverb}."
    
    # Return the completed Mad Lib as a JSON response
    return Response(madlib, status=status.HTTP_201_CREATED)
