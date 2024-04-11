from openai import OpenAI
from api.services.i_trip_suggestion_service import ITripSuggestionService
from api.repositories.i_trips_repository import ITripsRepository

class TripsService: 
    def __init__(self, trips_repository: ITripsRepository, trip_suggestion_service: ITripSuggestionService):
        self.repository = trips_repository
        self.trip_suggestion_service = trip_suggestion_service
        
    def get_suggestion(self, messages):
        suggestion = self.trip_suggestion_service.get_trip_suggestion(messages)
        
        self.repository.save_suggestion(suggestion)

        return suggestion