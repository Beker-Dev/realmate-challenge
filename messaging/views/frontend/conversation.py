from django.views.generic import ListView
from messaging.models import ConversationModel


class ConversationListView(ListView):
    model = ConversationModel
    template_name = 'conversation/list.html'
    ordering = ['-updated_at']
    queryset = ConversationModel.objects.all()
