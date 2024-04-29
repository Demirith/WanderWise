from api.services.i_trip_suggestion_service import ITripSuggestionService
class TripsService: 
    def __init__(self, trip_suggestion_service: ITripSuggestionService):
        self.trip_suggestion_service = trip_suggestion_service
        
    def get_suggestion(self, messages):
        suggestion = self.trip_suggestion_service.get_trip_suggestion(messages)

        return suggestion