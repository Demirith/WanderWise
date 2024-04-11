from django.test import TestCase
from unittest.mock import mock_open, patch, Mock, call
from api.repositories.trips_repository import TripsRepository
from api.models import Suggestion

class TestTripsRepository(TestCase):
    def setUp(self):
        self.response_message = Mock()
        self.response_message.content = "Test content"
        self.response_message.role = "Test role"
        
        self.test_suggestion = Suggestion("Test prompt", self.response_message, "Test model")
        self.test_class_instance = TripsRepository()

    data_to_return = '{"responses": []}'
    @patch("builtins.open", new_callable=mock_open, read_data=data_to_return.encode("utf-8"))
    def test_save_suggestion(self, mock_open):
        # Arrange
        json_file_path = "historical_responses.json"
        
        # Act
        self.test_class_instance.save_suggestion(self.test_suggestion)

        # Assert
        calls = [call(json_file_path, "r"), call(json_file_path, "w")]
        mock_open.assert_has_calls(calls, any_order=True)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_suggestion_missing_file(self, mock_open):
        # Arrange
        mock_open.side_effect = [FileNotFoundError(), mock_open()]
        json_file_path = "historical_responses.json"

        # Act
        self.test_class_instance.save_suggestion(self.test_suggestion)

        # Assert
        calls = [call(json_file_path, "r"), call(json_file_path, "w")]
        mock_open.assert_has_calls(calls, any_order=True)
  