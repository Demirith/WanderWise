class SuggestionData: 
    def __init__(self, start_destination: str, end_destination: str, duration: str, budget: str, points_of_interest: str, interests: str):
        self.start_destination = start_destination
        self.end_destination = end_destination
        self.duration = duration
        self.budget = budget
        self.points_of_interest = points_of_interest
        self.interests = interests
        
    @classmethod
    def convert_data_to_suggestion(cls, data):
        return cls(
            start_destination=data.get('start_destination'),
            end_destination=data.get('end_destination'),
            duration=data.get('duration'),
            budget=data.get('budget'),
            points_of_interest=data.get('points_of_interest'),
            interests=data.get('interests')
        )