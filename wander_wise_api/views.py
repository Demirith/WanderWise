from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .service_locator import service_locator

@api_view(['GET'])
def suggestion(request, service_locator=service_locator):
    messages = [
        {"role": "user", "content": "Advice on a trip with the given information"},
        {"role": "user", "content": "Start Destination: Tokyo"},
        {"role": "user", "content": "End Destination: Kyoto"},
        {"role": "user", "content": "Duration: 4 weeks"},
        {"role": "user", "content": "Budget: $7000"},
        {"role": "user", "content": "Points of Interest: Mount Fuji, Kyoto"},
        {"role": "user", "content": "Interests: Hiking, Fishing, Food, Sleeping in a ryokan"}
    ]    
    
    trips_service = service_locator.get_service('trips_service')
    suggestion_response = trips_service.get_suggestion(messages)

    return Response(suggestion_response.to_dict())