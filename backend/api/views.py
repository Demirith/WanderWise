from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .service_locator import service_locator
from api.dto.suggestion_dto import SuggestionDTO
from api.types.suggestion_types import SuggestionData
from api.utils.data_processing import construct_message

@api_view(['POST'])
def suggestion(request, service_locator=service_locator):
    data = request.data
    
    try:
        suggestionData = SuggestionData.convert_data_to_suggestion(data)
        messages = construct_message(suggestionData)
        
        trips_service = service_locator.get_service('trips_service')
        suggestion = trips_service.get_suggestion(messages)

        suggestion_response = SuggestionDTO.from_suggestion(suggestion) 
        return Response(suggestion_response.to_dict())
    except Exception as e:
        print(f"An error occurred: {e}")
        return Response({"error": "An error occurred while processing the request"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)