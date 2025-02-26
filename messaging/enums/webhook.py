from django.db import models


class WebhookEventType(models.TextChoices):
    NEW_CONVERSATION = "NEW_CONVERSATION", "New Conversation"
    CLOSE_CONVERSATION = "CLOSE_CONVERSATION", "Close Conversation"
    NEW_MESSAGE = "NEW_MESSAGE", "New Message"
    