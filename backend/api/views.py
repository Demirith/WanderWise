from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django_ratelimit.decorators import ratelimit
from .service_locator import service_locator
from api.dto.suggestion_dto import SuggestionDTO
from api.types.suggestion_types import SuggestionData
from api.utils.data_processing import construct_message

# Just for testing
def conditional_ratelimit(*args, **kwargs):
    if settings.TESTING:
        # Return the function unchanged if in testing mode
        return lambda func: func
    else:
        # Apply ratelimit otherwise
        return ratelimit(*args, **kwargs)

@conditional_ratelimit(key='ip', rate='1/m')
@api_view(['POST'])
def suggestion(request, service_locator=service_locator):
    data = request.data
    
    try:
        suggestionData = SuggestionData.convert_data_to_suggestion(data)
        messages = construct_message(suggestionData)
        
        trips_service = service_locator.get_service('trips_service')
        suggestion = trips_service.get_suggestion(messages)

        suggestion_response = SuggestionDTO.from_suggestion(suggestion) 
        return JsonResponse(suggestion_response.to_dict())
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)