from django.db import models

# Create your models here.
class Suggestion:
    def __init__(self, prompt, response_message, model_used):
        self.prompt = prompt
        self.content = response_message.content
        self.role = response_message.role
        self.model_used = model_used
        
    def to_dict(self):
        return {
            "prompt": self.prompt,
            "content": self.content,
            "role": self.role,
            "model_used": self.model_used
        }