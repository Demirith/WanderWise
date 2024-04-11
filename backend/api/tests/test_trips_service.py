import json 
from django.test import TestCase
from unittest.mock import Mock
from api.services.trips_service import TripsService
from api.services.i_trip_suggestion_service import ITripSuggestionService
from api.repositories.i_trips_repository import ITripsRepository

class TestTripsService(TestCase):
    def setUp(self):
        self.mock_repository = Mock(spec=ITripsRepository)
        self.mock_suggestion_service = Mock(spec=ITripSuggestionService)
        self.service = TripsService(self.mock_repository, self.mock_suggestion_service)

    def test_get_suggestion(self):
        # Arrange
        test_messages = [
            {"role": "user", "content": "Start Destination: Tokyo"},
            {"role": "user", "content": "End Destination: Kyoto"}
        ]
        
        mock_response = Mock()
        mock_response.prompt = json.dumps(test_messages)
        mock_response.content = "Test content"
        mock_response.role = "Test role"
        mock_response.model_used = "Test model"
        self.mock_suggestion_service.get_trip_suggestion.return_value = mock_response

        # Act
        result = self.service.get_suggestion(test_messages)

        # Assert
        self.assertEqual(result.prompt, mock_response.prompt)
        self.assertEqual(result.content, mock_response.content)
        self.assertEqual(result.role, mock_response.role)
        self.assertEqual(result.model_used, mock_response.model_used)
        
        self.mock_suggestion_service.get_trip_suggestion.assert_called_once_with(test_messages)
        self.mock_repository.save_suggestion.assert_called_once_with(mock_response)