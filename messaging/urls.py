from django.urls import path
from . import views


app_name='messaging'
urlpatterns = [
    path('webhook', views.WebhookView.as_view(), name='messaging-webhook'),
    path('conversations', views.ConversationView.as_view(), name='messaging-conversation-list'),
    path('conversations/<uuid:pk>', views.ConversationView.as_view(), name='messaging-conversation-detail'),
]
