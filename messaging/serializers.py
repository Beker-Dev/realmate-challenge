from rest_framework import serializers
from .models import (
    ConversationModel,
    MessageModel
)

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationModel
        fields = ['id', 'type', 'state']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ['id', 'content', 'direction', 'conversation_id']
