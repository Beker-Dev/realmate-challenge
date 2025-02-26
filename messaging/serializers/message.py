from rest_framework import serializers
from messaging.models import MessageModel


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ['id', 'content', 'direction', 'conversation_id']
        