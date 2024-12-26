from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import uuid

class Role(models.TextChoices):
    GUEST = 'Guest', 'Guest'
    HOST = 'Host', 'Host'
    ADMIN = 'Admin', 'Admin'

# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=64, unique=True)
    role = models.TextField(choices=Role, default=Role.GUEST, null=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True)

class Message(models.Model):
    message_id = models.UUIDField(max_length=36, primary_key=True, unique=True, db_index=True, default=uuid.uuid4())
    message_body = models.TextField(max_length=255, null=False)
    sent_at = models.DateTimeField(auto_now=True)
    sender_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

class Conversation(models.Model):
    conversation_id = models.UUIDField(max_length=36, primary_key=True, unique=True, db_index=True, default=uuid.uuid4())
    created_at = models.DateTimeField(auto_now=True)
    participants_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
