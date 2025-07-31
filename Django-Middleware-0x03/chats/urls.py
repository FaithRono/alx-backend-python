from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from .views import UserViewSet, ConversationViewSet, MessageViewSet, ConversationMessagesViewSet

# Create a DefaultRouter and register our viewsets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Create a NestedDefaultRouter for nested routes
conversations_router = nested_routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversations_router.register(r'messages', ConversationMessagesViewSet, basename='conversation-messages')

# Define URL patterns
urlpatterns = [
    # Include all router URLs (automatically creates CRUD endpoints)
    path('', include(router.urls)),
    
    # Include nested router URLs
    path('', include(conversations_router.urls)),
]