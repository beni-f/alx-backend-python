from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import uuid 
# Create your models here.
class Role(models.TextChoices):
    GUEST = 'guest', 'guest'
    HOST = 'host', 'host'
    ADMIN = 'admin', 'admin'

class User(AbstractUser):
    email = models.CharField(max_length=64, null=False, unique=True, db_index=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=15, choices=Role.choices, default=Role.GUEST, null=False)
    created_at = models.DateTimeField(auto_now=True)

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), db_index=True)
    participants_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)

class Message(models.Model):

    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), db_index=True)
    message_body = models.TextField(max_length=200, null=False)
    sent_at = models.DateTimeField(auto_now=True)
    conversation_id = models.ForeignKey(
        Conversation,
        models.CASCADE,
        null=True
    )
    sender_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
