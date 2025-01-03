from django.shortcuts import render
from rest_framework import viewsets, response, exceptions
from .models import Conversation, Message
from .serializers import MessageSerializer, ConversationSerializer

# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Conversation.objects.all()
        serializer = ConversationSerializer(queryset)
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Conversation.objects.all()
        conversation = Conversation.objects.get(pk=pk)
        serializer = ConversationSerializer(conversation)
        return response.Response(serializer.data)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            message = self.get_queryset().get(pk=pk)
        except Message.DoesNotExist:
            raise exceptions.NotFound(detail=f"Message with id {pk} not found.")
        serializer = self.get_serializer(message)
        return response.Response(serializer.data)
