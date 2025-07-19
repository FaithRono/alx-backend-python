from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ConversationViewSet, MessageViewSet, ConversationMessagesViewSet

# Create a router and register our viewsets with DefaultRouter
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Define URL patterns
urlpatterns = [
    # Include all router URLs (automatically creates CRUD endpoints)
    path('', include(router.urls)),
    
    # Custom nested routes for conversation messages
    path('conversations/<uuid:conversation_id>/messages/', 
         ConversationMessagesViewSet.as_view({'get': 'list'}), 
         name='conversation-messages'),
]