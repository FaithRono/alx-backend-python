from rest_framework import permissions
from rest_framework.permissions import BasePermission
from .models import Conversation, Message


class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to only allow participants of a conversation to access it.
    """
    
    def has_permission(self, request, view):
        """Check if user is authenticated."""
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        """Check if user is participant of the conversation."""
        if isinstance(obj, Conversation):
            return obj.participants.filter(user_id=request.user.user_id).exists()
        elif isinstance(obj, Message):
            return obj.conversation.participants.filter(user_id=request.user.user_id).exists()
        return False


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only to the owner of the object
        if hasattr(obj, 'sender'):  # For Message objects
            return obj.sender == request.user
        elif hasattr(obj, 'user'):  # For objects with user field
            return obj.user == request.user
        
        return False


class IsMessageSender(BasePermission):
    """
    Custom permission to only allow message senders to edit/delete their messages.
    """
    
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Message):
            return obj.sender == request.user
        return False


class IsConversationParticipant(BasePermission):
    """
    Permission class to check if user is participant in conversation.
    """
    
    def has_permission(self, request, view):
        """Check if user is authenticated."""
        if not request.user or not request.user.is_authenticated:
            return False
        
        # For list views, check if conversation_id is in query params
        conversation_id = request.query_params.get('conversation_id')
        if conversation_id:
            try:
                conversation = Conversation.objects.get(conversation_id=conversation_id)
                return conversation.participants.filter(user_id=request.user.user_id).exists()
            except Conversation.DoesNotExist:
                return False
        
        return True
    
    def has_object_permission(self, request, view, obj):
        """Check object-level permission."""
        if isinstance(obj, Message):
            return obj.conversation.participants.filter(user_id=request.user.user_id).exists()
        elif isinstance(obj, Conversation):
            return obj.participants.filter(user_id=request.user.user_id).exists()
        
        return False


class CanCreateConversation(BasePermission):
    """
    Permission to allow authenticated users to create conversations.
    """
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class CanSendMessage(BasePermission):
    """
    Permission to allow participants to send messages to conversations.
    """
    
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Check if user is participant of the conversation they're trying to send message to
        if request.method == 'POST':
            conversation_id = request.data.get('conversation')
            if conversation_id:
                try:
                    conversation = Conversation.objects.get(conversation_id=conversation_id)
                    return conversation.participants.filter(user_id=request.user.user_id).exists()
                except Conversation.DoesNotExist:
                    return False
        
        return True