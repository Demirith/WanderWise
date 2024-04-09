import json
from wander_wise_api.repositories.i_trips_repository import ITripsRepository

class TripsRepository(ITripsRepository): 
    def save_suggestion(self, suggestion_response): 
        json_file_path = "historical_responses.json"

        try:
            with open(json_file_path, "r") as file:
                historical_responses = json.load(file)
        except FileNotFoundError:
            historical_responses = {"responses": []}

        historical_responses["responses"].append(suggestion_response.to_dict())

        with open(json_file_path, "w") as file:
            json.dump(historical_responses, file, indent=4)
