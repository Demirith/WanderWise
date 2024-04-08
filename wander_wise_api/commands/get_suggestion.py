#handle dependecy injection
from wander_wise_api.services.TripsService import TripsService
from wander_wise_api.services.OpenAIService import OpenAIService
from wander_wise_api.repositories.TripsRepository import TripsRepository

def generate_trip_suggestion(messages):
    #Where to inject this?
    open_ai_service = OpenAIService()
    trips_repository = TripsRepository()
    trips_service = TripsService(trips_repository, open_ai_service)

    suggestion_response = trips_service.get_suggestion(messages)
    
    return suggestion_response

