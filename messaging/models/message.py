from django.db import models
from messaging.enums import MessageDirection
from messaging.models.abstract import AbstractModel
from messaging.models.conversation import ConversationModel


class MessageModel(AbstractModel):
    content = models.TextField()
    direction = models.CharField(max_length=8, choices=MessageDirection.choices)
    conversation_id = models.ForeignKey(ConversationModel, on_delete=models.CASCADE, related_name='messages')
