from rest_framework import serializers
from api.types.suggestion_types import SuggestionData


class SuggestionDataSerializer(serializers.Serializer):
    start_destination = serializers.CharField(max_length=100)
    end_destination = serializers.CharField(max_length=100)
    duration = serializers.CharField(max_length=50)
    budget = serializers.CharField(max_length=50)
    points_of_interest = serializers.CharField(max_length=200)
    interests = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return SuggestionData(**validated_data)
