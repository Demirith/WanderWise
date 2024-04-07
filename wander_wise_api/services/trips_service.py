
from openai import OpenAI
    
class TripsService: 
    def __init__(self, trips_repository, open_ai_service):
        self.repository =  trips_repository
        self.open_ai_service = open_ai_service
        
    def get_suggestion(self, messages):
        suggestion_response = self.open_ai_service.get_suggestion_from_open_ai(messages)
        
        print(suggestion_response.content)
        
        self.repository.save_suggestion(suggestion_response)

        return suggestion_response