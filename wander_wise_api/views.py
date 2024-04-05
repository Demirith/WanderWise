from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .actions import openai

# Create your views here.
@api_view(['GET'])
def suggestion(request): 
    data = openai.generate_trip_suggestion()
    return Response(data)