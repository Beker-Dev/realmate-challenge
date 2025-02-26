from django.db import models

class ConversationType(models.TextChoices):
    NEW_CONVERSATION = "NEW_CONVERSATION", "New Conversation"
    CLOSE_CONVERSATION = "CLOSE_CONVERSATION", "Close Conversation"


class ConversationState(models.TextChoices):
    OPEN = "OPEN", "Open"
    CLOSED = "CLOSED", "Closed"
    

class MessageDirection(models.TextChoices):
    SENT = "SENT", "Sent"
    RECEIVED = "RECEIVED", "Received"


class WebhookEventType(models.TextChoices):
    NEW_CONVERSATION = "NEW_CONVERSATION", "New Conversation"
    CLOSE_CONVERSATION = "CLOSE_CONVERSATION", "Close Conversation"
    NEW_MESSAGE = "NEW_MESSAGE", "New Message"
    