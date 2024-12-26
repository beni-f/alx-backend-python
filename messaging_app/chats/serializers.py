from .models import User, Conversation, Message
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants']

class MessageSerializer(serializers.ModelSerializer):
    conversation = ConversationSerializer()
    sender = UserSerializer()
    class Meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender']

    def create(self, validated_data):
        conversation_data = validated_data.pop('conversation')
        sender_data = validated_data.pop('sender')

        conversation, _ = Conversation.objects.get_or_create(**conversation_data)

        sender, _ = User.objects.get_or_create(**sender_data)

        message = Message.objects.create(conversation=conversation, sender=sender, **validated_data)

        return message
