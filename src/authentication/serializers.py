# serializers.py
from rest_framework import serializers

class GenerateTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)

    def validate_username(self, value):
        # Validate username as needed
        if not value:
            raise serializers.ValidationError("Username must be provided")
        return value
