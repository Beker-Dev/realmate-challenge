from django.db import models
from messaging.enums import ConversationState
from messaging.models.abstract import AbstractModel


class ConversationModel(AbstractModel):
    state = models.CharField(max_length=6, choices=ConversationState.choices)
