from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers as nested_routers

from .views import UserViewSet, ConversationViewSet, MessageViewSet, ConversationMessagesViewSet

# Create a DefaultRouter and register our viewsets
router = DefaultRouter()
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

# The DefaultRouter automatically creates these endpoints:
# GET    /users/                     - List all users
# POST   /users/                     - Create a new user
# GET    /users/{user_id}/           - Retrieve a specific user
# PUT    /users/{user_id}/           - Update a specific user
# PATCH  /users/{user_id}/           - Partially update a specific user
# DELETE /users/{user_id}/           - Delete a specific user

# GET    /conversations/             - List all conversations
# POST   /conversations/             - Create a new conversation
# GET    /conversations/{conversation_id}/     - Retrieve a specific conversation
# PUT    /conversations/{conversation_id}/     - Update a specific conversation
# PATCH  /conversations/{conversation_id}/     - Partially update a specific conversation
# DELETE /conversations/{conversation_id}/     - Delete a specific conversation
# POST   /conversations/{conversation_id}/add_participant/    - Add participant (custom action)
# POST   /conversations/{conversation_id}/remove_participant/ - Remove participant (custom action)
# GET    /conversations/{conversation_id}/messages/           - Get conversation messages (custom action)

# GET    /messages/                  - List all messages
# POST   /messages/                  - Create a new message (send message to existing conversation)
# GET    /messages/{message_id}/     - Retrieve a specific message
# PUT    /messages/{message_id}/     - Update a specific message
# PATCH  /messages/{message_id}/     - Partially update a specific message
# DELETE /messages/{message_id}/     - Delete a specific message
# GET    /messages/by_conversation/  - Get messages by conversation (custom action)
# PATCH  /messages/{message_id}/mark_as_read/ - Mark message as read (custom action)

# NestedDefaultRouter creates:
# GET    /conversations/{conversation_id}/messages/  - List messages for specific conversation
# POST   /conversations/{conversation_id}/messages/  - Create message in specific conversation