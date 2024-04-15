from typing import Dict, List
from api.types.suggestion_types import SuggestionData

def construct_message(data: SuggestionData) -> List[Dict]: 
    messages = [
        {"role": "user", "content": "Advice on a trip with the given information"},
        {"role": "user", "content": f"Start Destination: {data.start_destination}"},
        {"role": "user", "content": f"End Destination: {data.end_destination}"},
        {"role": "user", "content": f"Duration: {data.duration}"},
        {"role": "user", "content": f"Budget: {data.budget}"},
        {"role": "user", "content": f"Points of Interest: {data.points_of_interest}"},
        {"role": "user", "content": f"Interests: {data.interests}"}
    ]
    return messages