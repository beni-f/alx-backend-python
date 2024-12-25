from django.contrib import admin
from .models import Conversation, Message, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('first_name', 'last_name', 'username', 'email', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('role', 'phone_number', 'created_at'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('role', 'phone_number'),
        }),
    )
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(User, CustomUserAdmin)