from abc import ABC, abstractmethod

class ITripsRepository(ABC):
    @abstractmethod
    def save_suggestion(self, suggestion_response):
        pass