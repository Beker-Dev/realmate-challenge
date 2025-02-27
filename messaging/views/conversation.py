from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from messaging.models import ConversationModel
from messaging.serializers import ConversationSerializer

    
class ConversationView(APIView):
    def get(self, request, pk=None):
        if not pk:
            db_conversation_list = ConversationModel.objects.all()
            serializer = ConversationSerializer(db_conversation_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        db_conversation = get_object_or_404(ConversationModel, pk=pk)
        serializer = ConversationSerializer(db_conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)
    