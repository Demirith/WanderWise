import json
from django.test import TestCase
from unittest.mock import patch, Mock
from api.services.open_ai_service import OpenAIService
from api.models import Suggestion

class TestOpenAIService(TestCase):
    def setUp(self):
        self.openai_service = OpenAIService()

    @patch('api.models.Suggestion.objects.create')
    def test_get_trip_suggestion(self, mock_create):
        # Arrange
        mock_openai_client = Mock()
        mock_completion = Mock()
        mock_message = Mock()
        
        mock_message.content = "Suggestion message"
        mock_message.role = "assistant"
        mock_completion.choices = [Mock(message=mock_message)]
        mock_completion.model = "gpt-3.5-turbo"
        mock_openai_client.chat.completions.create.return_value = mock_completion
        self.openai_service.client = mock_openai_client
        
        mock_suggestion = Mock()
        mock_suggestion.prompt = json.dumps([
            {"role": "user", "content": "Start Destination: Tokyo"},
            {"role": "user", "content": "End Destination: Kyoto"}
        ])
        mock_suggestion.content = "Suggestion message"
        mock_suggestion.role = "assistant"
        mock_suggestion.model_used = "gpt-3.5-turbo"
        mock_create.return_value = mock_suggestion
        
        messages = [
            {"role": "user", "content": "Start Destination: Tokyo"},
            {"role": "user", "content": "End Destination: Kyoto"}
        ]

        # Act
        suggestion_response = self.openai_service.get_trip_suggestion(messages)

        # Assert
        self.assertEqual(suggestion_response.prompt, json.dumps(messages))
        self.assertEqual(suggestion_response.content, "Suggestion message")
        self.assertEqual(suggestion_response.role, "assistant")
        self.assertEqual(suggestion_response.model_used, "gpt-3.5-turbo")

        mock_create.assert_called_once_with(
            trip=None,
            user=None,
            prompt=json.dumps(messages),
            content="Suggestion message",
            role="assistant",
            model_used="gpt-3.5-turbo"
        )