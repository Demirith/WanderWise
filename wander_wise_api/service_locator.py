from wander_wise_api.services.trips_service import TripsService
from wander_wise_api.services.open_ai_service import OpenAIService
from wander_wise_api.repositories.trips_repository import TripsRepository

class ServiceLocator: 
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._services = {}
        return cls._instance
    
    def register_service(self, name, service):
        self._services[name] = service
        
    def get_service(self, name):
        return self._services.get(name)
    
service_locator = ServiceLocator()
open_ai_service = OpenAIService()
trips_repository = TripsRepository()

service_locator.register_service('open_ai_service', open_ai_service)
service_locator.register_service('trips_repository', trips_repository)
service_locator.register_service('trips_service', TripsService(trips_repository, open_ai_service))