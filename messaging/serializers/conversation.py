from rest_framework import serializers
from messaging.models import ConversationModel
from messaging.serializers.message import MessageSerializer

        
class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True) 

    class Meta:
        model = ConversationModel
        fields = ['id', 'state', 'messages']
