class SuggestionDTO:
    def __init__(self, prompt, content, role, model_used):
        self.prompt = prompt
        self.content = content
        self.role = role
        self.model_used = model_used
        
    def from_suggestion(cls, suggestion):
        return cls(
            prompt=suggestion.prompt,
            content=suggestion.content,
            role=suggestion.role,
            model_used=suggestion.model_used
        )
    
    def to_dict(self):
        return {
            "prompt": self.prompt,
            "content": self.content,
            "role": self.role,
            "model_used": self.model_used
        }