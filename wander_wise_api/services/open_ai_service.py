import json
from openai import OpenAI
from wander_wise_api.models import Suggestion
from wander_wise_api.services.i_trip_suggestion_service import ITripSuggestionService

class OpenAIService(ITripSuggestionService):
    def __init__(self) -> None:
        self.client = OpenAI() 
    
    def get_trip_suggestion(self, messages):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
        
        response_message = completion.choices[0].message
        model_used = completion.model
        suggestion_response = Suggestion(json.dumps(messages), response_message, model_used)
        
        return suggestion_response
