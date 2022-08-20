from rest_framework import serializers

# import model from models.py
from .models import ChatModel


# Create a model serializer
class ChatBotSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = ChatModel
        fields = ('query', 'result')
