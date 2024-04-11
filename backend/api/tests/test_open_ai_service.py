import json
from django.test import TestCase
from unittest.mock import Mock
from api.services.open_ai_service import OpenAIService

class TestOpenAIService(TestCase):
    def setUp(self):
        self.openai_service = OpenAIService()

    def test_get_trip_suggestion(self):
        # Arrange
        mock_message = Mock()
        mock_message.message.content = "Suggestion message"
        mock_message.message.role = "assistant"
        
        mock_completion = Mock()
        mock_completion.choices = [mock_message]
        mock_completion.model = "gpt-3.5-turbo"
        
        mock_openai_client = Mock()
        mock_openai_client.chat.completions.create.return_value = mock_completion
        self.openai_service.client = mock_openai_client

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

