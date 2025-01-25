from .models import User, Conversation, Message
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'role', 'phone_number']

class ConversationSerializer(serializers.ModelSerializer):
    participants_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Conversation
        fields = ['participants_id', 'created_at']


    

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [ 'conversation_id', 'message_id', 'sender_id', 'message_body', 'sent_at']
        extra_kwargs = {
            'message_id': {'read_only': True},
        }
