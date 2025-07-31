from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet, ConversationViewSet, MessageViewSet

# Create a DefaultRouter and register our viewsets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Define URL patterns
urlpatterns = [
    # JWT Authentication endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Include all router URLs (automatically creates CRUD endpoints)
    path('', include(router.urls)),
    
    # Custom endpoints for message filtering
    path('messages/by_conversation/', MessageViewSet.as_view({'get': 'by_conversation'}), name='messages-by-conversation'),
]