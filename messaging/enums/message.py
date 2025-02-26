from django.db import models


class MessageDirection(models.TextChoices):
    SENT = "SENT", "Sent"
    RECEIVED = "RECEIVED", "Received"
