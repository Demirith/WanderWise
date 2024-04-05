from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .commands import suggestion

# Create your views here.
@api_view(['GET'])
def suggestion(request): 
    data = suggestion.generate_trip_suggestion()
    return Response(data)