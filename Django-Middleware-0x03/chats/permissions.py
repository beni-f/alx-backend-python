from rest_framework.permissions import BasePermission

from rest_framework.permissions import SAFE_METHODS
class IsSender(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.sender_id

class IsParticipantOfConversation(BasePermission):
    def has_permission(self, request, view):
        return request.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return request.user.id in obj.participants_id
