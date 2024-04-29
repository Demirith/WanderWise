from api.services.trips_service import TripsService
from api.services.open_ai_service import OpenAIService

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

service_locator.register_service('open_ai_service', open_ai_service)
service_locator.register_service('trips_service', TripsService(open_ai_service))