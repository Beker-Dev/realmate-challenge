from django.urls import path
from messaging import views


app_name='messaging'
urlpatterns = [
    path('', views.frontend.ConversationListView.as_view(), name='conversation-list-view'),
    path('webhook', views.WebhookView.as_view(), name='webhook'),
    path('conversations', views.ConversationView.as_view(), name='conversation-list'),
    path('conversations/<uuid:pk>', views.ConversationView.as_view(), name='conversation-detail'),
]
