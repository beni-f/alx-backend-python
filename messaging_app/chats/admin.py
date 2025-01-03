from django.contrib import admin
from .models import Message, Conversation, User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'password_hash', 'role', 'phone_number', 'created_at')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Message)
admin.site.register(Conversation)
