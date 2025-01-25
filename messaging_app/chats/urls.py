from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ConversationViewSet

router = DefaultRouter()
router.register(r'message', MessageViewSet, basename='message')
router.register(r'conversation', ConversationViewSet, basename='conversation')

urlpatterns = router.urls