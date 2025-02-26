import uuid
from django.db import models
from .enums import (
    ConversationType,
    ConversationState,
    MessageDirection
)


class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

class ConversationModel(AbstractModel):
    type = models.CharField(max_length=18, choices=ConversationType.choices)
    state = models.CharField(max_length=6, choices=ConversationState.choices)


class MessageModel(AbstractModel):
    content = models.TextField()
    direction = models.CharField(max_length=8, choices=MessageDirection.choices)
    conversation_id = models.ForeignKey(ConversationModel, on_delete=models.CASCADE)
