from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import (
    WebhookEventSerializer,
    WebhookEventConversationDataSerializer,
    WebhookEventMessageDataSerializer
)
from .models import (
    ConversationModel,
    MessageModel
)
from .enums import (
    WebhookEventType,
    ConversationType,
    ConversationState,
    MessageDirection
)

class ConversationView(APIView):
    def get(self, request, pk, *args, **kwargs):
        db_conversation = get_object_or_404(ConversationModel, pk=pk)
        return Response(db_conversation, status=status.HTTP_200_OK)
    
class WebhookView(GenericAPIView):
    serializer_class = WebhookEventSerializer
    http_method_names = ['post']
    
    def _open_conversation(self, data: dict):
        if ConversationModel.objects.filter(id=data['id']).exists():
            raise APIException('Conversation already exists')
    
        ConversationModel(
            id=data['id'],
            type=ConversationType.NEW_CONVERSATION,
            state=ConversationState.OPEN
        ).save()
        
    def _close_conversation(self, data: dict):
        db_conversation = ConversationModel.objects.filter(id=data['id']).first()
        if not db_conversation:
            raise APIException('Conversation does not exist')
        
        if db_conversation.state == ConversationState.CLOSED:
            raise APIException('Conversation is already closed')

        db_conversation.state = ConversationState.CLOSED
        db_conversation.save()
        
    def _add_new_message(self, data: dict):
        db_conversation = ConversationModel.objects.filter(id=data['conversation_id']).first()
        if not db_conversation:
            raise APIException('Conversation does not exist')
        
        if db_conversation.state == ConversationState.CLOSED:
            raise APIException('Conversation is closed, it cannot have new messages')
    
        MessageModel(
            id=data['id'],
            content=data['content'],
            direction=data['direction'],
            conversation_id=db_conversation
        ).save()
    
    def _handle_webhook_event_type(self, serializer: WebhookEventSerializer):
        message = ""
        match serializer.data['type']:
            case WebhookEventType.NEW_CONVERSATION:
                self._open_conversation(WebhookEventConversationDataSerializer(data=serializer.data['conversation_data']).initial_data)
                message = "Conversation created"              
            case WebhookEventType.CLOSE_CONVERSATION:
                self._close_conversation(WebhookEventConversationDataSerializer(data=serializer.data['conversation_data']).initial_data)
                message = "Conversation closed"
            case WebhookEventType.NEW_MESSAGE:
                self._add_new_message(WebhookEventMessageDataSerializer(data=serializer.data['message_data']).initial_data)
                message = "Message added to conversation"
                
        return Response(message, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        try: 
            return self._handle_webhook_event_type(serializer)
        except (APIException, Exception) as e:
            if isinstance(e, APIException):
                return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
            return Response(f'Unexpected error: {e}', status=status.HTTP_400_BAD_REQUEST)
    