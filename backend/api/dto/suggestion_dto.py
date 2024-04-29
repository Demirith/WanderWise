class SuggestionDTO:
    def __init__(self, content):
        self.content = content
    
    @classmethod
    def from_suggestion(cls, suggestion):
        return cls(
            content=suggestion.content
        )
    
    def to_dict(self):
        return {
            "content": self.content
        }