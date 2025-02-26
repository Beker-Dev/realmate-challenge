from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ConversationView(APIView):
    def get(self, request, *args, **kwargs):
        return Response()

class WebhookView(APIView):
    def post(self, request, *args, **kwargs):
        return Response({'status': 'test'}, status=status.HTTP_201_CREATED)
    