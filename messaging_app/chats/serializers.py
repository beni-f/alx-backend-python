from .models import User, Conversation, Message
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'role', 'phone_number']

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['participants_id', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    conversation = serializers.PrimaryKeyRelatedField(
        queryset = Conversation.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = Message
        fields = ['conversation', 'message_id', 'sender_id', 'message_body', 'sent_at']
        extra_kwargs = {'message_id': {'read_only': True}}

    def create(self, validated_data):
        conversation_data = self.validated_data.pop('conversation')
        conversation, _ = Conversation.objects.get_or_create(**conversation_data)
        message, _ = Message.objects.create(conversation=conversation, **validated_data)
        return message
