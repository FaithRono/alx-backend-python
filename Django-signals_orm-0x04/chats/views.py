from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Conversation, Message
from .serializers import (
    UserSerializer, 
    ConversationSerializer, 
    ConversationListSerializer,
    MessageSerializer, 
    MessageCreateSerializer
)
from .permissions import (
    IsParticipantOfConversation,
    IsOwnerOrReadOnly,
    IsMessageSender,
    IsConversationParticipant,
    CanCreateConversation,
    CanSendMessage
)
from .filters import MessageFilter, ConversationFilter, UserFilter
from .pagination import CustomPagination

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for managing users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user_id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = UserFilter
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['created_at', 'username']
    ordering = ['-created_at']
    
    from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Welcome to Messaging App API</h1>
        <p>Available endpoints:</p>
        <ul>
            <li><a href="/api/">API Root</a></li>
            <li><a href="/admin/">Admin Panel</a></li>
        </ul>
    """)
    
    def get_queryset(self):
        """Filter users based on current user's permissions."""
        if self.request.user.role == 'admin':
            return User.objects.all()
        return User.objects.filter(user_id=self.request.user.user_id)


class ConversationViewSet(viewsets.ModelViewSet):
    """ViewSet for managing conversations."""
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    lookup_field = 'conversation_id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ConversationFilter
    search_fields = ['participants__username']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-updated_at']
    
    def get_queryset(self):
        """Return conversations where the current user is a participant."""
        return Conversation.objects.filter(
            participants=self.request.user
        ).distinct().order_by('-updated_at')
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return ConversationListSerializer
        return ConversationSerializer
    
    def get_permissions(self):
        """Return appropriate permissions based on action."""
        if self.action == 'create':
            permission_classes = [IsAuthenticated, CanCreateConversation]
        else:
            permission_classes = [IsAuthenticated, IsParticipantOfConversation]
        
        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        """Create a new conversation."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Add current user to participants if not already included
        participant_ids = serializer.validated_data.get('participant_ids', [])
        if request.user.user_id not in participant_ids:
            participant_ids.append(request.user.user_id)
            serializer.validated_data['participant_ids'] = participant_ids
        
        conversation = serializer.save()
        
        # Return detailed conversation data
        response_serializer = ConversationSerializer(conversation)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsParticipantOfConversation])
    def add_participant(self, request, conversation_id=None):
        """Add a participant to the conversation."""
        conversation = self.get_object()
        user_id = request.data.get('user_id')
        
        if not user_id:
            return Response(
                {'error': 'user_id is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = User.objects.get(user_id=user_id)
            conversation.participants.add(user)
            
            serializer = ConversationSerializer(conversation)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response(
                {'error': 'User not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsParticipantOfConversation])
    def remove_participant(self, request, conversation_id=None):
        """Remove a participant from the conversation."""
        conversation = self.get_object()
        user_id = request.data.get('user_id')
        
        if not user_id:
            return Response(
                {'error': 'user_id is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = User.objects.get(user_id=user_id)
            conversation.participants.remove(user)
            
            serializer = ConversationSerializer(conversation)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response(
                {'error': 'User not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated, IsParticipantOfConversation])
    def messages(self, request, conversation_id=None):
        """Get all messages for a specific conversation with pagination."""
        conversation = self.get_object()
        messages = conversation.messages.all().order_by('sent_at')
        
        # Apply pagination
        paginator = CustomPagination()
        page = paginator.paginate_queryset(messages, request)
        if page is not None:
            serializer = MessageSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for managing messages."""
    permission_classes = [IsAuthenticated, IsConversationParticipant]
    lookup_field = 'message_id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = MessageFilter
    search_fields = ['message_body', 'sender__username']
    ordering_fields = ['sent_at']
    ordering = ['-sent_at']
    pagination_class = CustomPagination
    
    def get_queryset(self):
        """Return messages from conversations where the current user is a participant."""
        user_conversations = Conversation.objects.filter(
            participants=self.request.user
        )
        return Message.objects.filter(
            conversation__in=user_conversations
        ).select_related('sender', 'conversation').order_by('-sent_at')
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'create':
            return MessageCreateSerializer
        return MessageSerializer
    
    def get_permissions(self):
        """Return appropriate permissions based on action."""
        if self.action == 'create':
            permission_classes = [IsAuthenticated, CanSendMessage]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessageSender]
        else:
            permission_classes = [IsAuthenticated, IsConversationParticipant]
        
        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        """Send a new message to an existing conversation."""
        serializer = self.get_serializer(
            data=request.data, 
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        message = serializer.save()
        
        # Return detailed message data
        response_serializer = MessageSerializer(message)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'])
    def by_conversation(self, request):
        """Get messages filtered by conversation."""
        conversation_id = request.query_params.get('conversation_id')
        
        if not conversation_id:
            return Response(
                {'error': 'conversation_id parameter is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            conversation = Conversation.objects.get(
                conversation_id=conversation_id,
                participants=request.user
            )
            messages = self.get_queryset().filter(conversation=conversation)
            
            # Apply pagination
            page = self.paginate_queryset(messages)
            if page is not None:
                serializer = MessageSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Conversation.DoesNotExist:
            return Response(
                {'error': 'Conversation not found or you are not a participant'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=True, methods=['patch'])
    def mark_as_read(self, request, message_id=None):
        """Mark a message as read (placeholder for future functionality)."""
        message = self.get_object()
        
        # This is a placeholder for read status functionality
        # You would implement read tracking in your model
        return Response(
            {'message': 'Message marked as read'}, 
            status=status.HTTP_200_OK
        )
    
    def update(self, request, *args, **kwargs):
        """Update message (only allow if user is the sender)."""
        message = self.get_object()
        
        if message.sender != request.user:
            return Response(
                {'error': 'You can only edit your own messages'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """Delete message (only allow if user is the sender)."""
        message = self.get_object()
        
        if message.sender != request.user:
            return Response(
                {'error': 'You can only delete your own messages'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        return super().destroy(request, *args, **kwargs)


class ConversationMessagesViewSet(viewsets.ReadOnlyModelViewSet):
    """Specialized ViewSet for getting messages within a specific conversation."""
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sent_at']
    ordering = ['sent_at']
    pagination_class = CustomPagination
    
    def get_queryset(self):
        """Get messages for a specific conversation."""
        conversation_id = self.kwargs.get('conversation_conversation_id')
        
        # Ensure user is participant in the conversation
        conversation = get_object_or_404(
            Conversation,
            conversation_id=conversation_id,
            participants=self.request.user
        )
        
        return Message.objects.filter(
            conversation=conversation
        ).select_related('sender').order_by('sent_at')