from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wander_wise_api.services.TripsService import TripsService
from wander_wise_api.services.OpenAIService import OpenAIService
from wander_wise_api.repositories.TripsRepository import TripsRepository

# Create your views here.
@api_view(['GET'])
def suggestion(request):
    #Where to inject this?
    open_ai_service = OpenAIService()
    trips_repository = TripsRepository()
    trips_service = TripsService(trips_repository, open_ai_service)

    messages = [
        {"role": "user", "content": "Advice on a trip with the given information"},
        {"role": "user", "content": "Start Destination: Tokyo"},
        {"role": "user", "content": "End Destination: Kyoto"},
        {"role": "user", "content": "Duration: 4 weeks"},
        {"role": "user", "content": "Budget: $7000"},
        {"role": "user", "content": "Points of Interest: Mount Fuji, Kyoto"},
        {"role": "user", "content": "Interests: Hiking, Fishing, Food, Sleeping in a ryokan"}
    ]    
    
    suggestion_response = trips_service.get_suggestion(messages)

    return Response(suggestion_response.to_dict())