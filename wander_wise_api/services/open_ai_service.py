import json
from openai import OpenAI
from wander_wise_api.models import Suggestion

class OpenAIService:
    def __init__(self):
        self.client = OpenAI() 
    
    def get_suggestion_from_open_ai(self, messages):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
        
        response_message = completion.choices[0].message
        model_used = completion.model
        suggestion_response = Suggestion(json.dumps(messages), response_message, model_used)
        
        return suggestion_response
