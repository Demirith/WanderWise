from openai import OpenAI
from wander_wise_api.services.IOpenAIService import IOpenAIService
from wander_wise_api.repositories.ITripsRepository import ITripsRepository

class TripsService: 
    def __init__(self, trips_repository: ITripsRepository, open_ai_service: IOpenAIService):
        self.repository =  trips_repository
        self.open_ai_service = open_ai_service
        
    def get_suggestion(self, messages):
        suggestion_response = self.open_ai_service.get_suggestion_from_open_ai(messages)
        
        print(suggestion_response.content)
        
        self.repository.save_suggestion(suggestion_response)

        return suggestion_response