from abc import ABC, abstractmethod

class IOpenAIService(ABC):
    @abstractmethod
    def get_suggestion_from_open_ai(self, messages):
        pass