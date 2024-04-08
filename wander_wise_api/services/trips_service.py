from openai import OpenAI
from wander_wise_api.services.i_trip_suggestion_service import ITripSuggestionService
from wander_wise_api.repositories.i_trips_repository import ITripsRepository

class TripsService: 
    def __init__(self, trips_repository: ITripsRepository, trip_suggestion_service: ITripSuggestionService):
        self.repository =  trips_repository
        self.trip_suggestion_service = trip_suggestion_service
        
    def get_suggestion(self, messages):
        suggestion_response = self.trip_suggestion_service.get_trip_suggestion(messages)
        
        print(suggestion_response.content)
        
        self.repository.save_suggestion(suggestion_response)

        return suggestion_response