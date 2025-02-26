from rest_framework import serializers, exceptions
from .models import (
    ConversationModel,
    MessageModel
)
from .enums import (
    WebhookEventType
)

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationModel
        fields = ['id', 'type', 'state']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ['id', 'content', 'direction', 'conversation_id']

class WebhookEventConversationDataSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    
class WebhookEventMessageDataSerializer(MessageSerializer):
    id = serializers.UUIDField()

class WebhookEventSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=WebhookEventType.choices)
    timestamp = serializers.DateTimeField(required=False)
    data = serializers.JSONField()
    conversation_data = serializers.SerializerMethodField()
    message_data = serializers.SerializerMethodField()
    
    class Meta:
        swagger_schema_fields = {
            "example": {
                "type": "NEW_CONVERSATION",
                "timestamp": "2024-02-26T12:34:56Z",
                "data": {
                    "id": "uuid-here",
                }
            }
        }
        
    def validate(self, attrs):
        match attrs['type']:
            case WebhookEventType.NEW_CONVERSATION:
                WebhookEventConversationDataSerializer(data=attrs['data']).is_valid(raise_exception=True)  
            case WebhookEventType.CLOSE_CONVERSATION:
                WebhookEventConversationDataSerializer(data=attrs['data']).is_valid(raise_exception=True)  
            case WebhookEventType.NEW_MESSAGE:
                WebhookEventMessageDataSerializer(data=attrs['data']).is_valid(raise_exception=True) 
            
        return super().validate(attrs)

    def get_conversation_data(self, obj):
        conversation_data = WebhookEventConversationDataSerializer(data=obj['data'])
        if conversation_data.is_valid():
            return conversation_data.data
        return None
    
    def get_message_data(self, obj):
        message_data = WebhookEventMessageDataSerializer(data=obj['data'])
        if message_data.is_valid():
            return message_data.data
        return None
    
    def to_representation(self, instance):
        return super().to_representation(instance)
    