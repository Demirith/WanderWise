from abc import ABC, abstractmethod

class ITripSuggestionService (ABC):
    @abstractmethod
    def get_trip_suggestion(self, messages):
        pass