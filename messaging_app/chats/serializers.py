from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    full_name = serializers.CharField(read_only=True, source='get_full_name')
    
    class Meta:
        model = User
        fields = [
            'user_id', 
            'username', 
            'email', 
            'first_name', 
            'last_name',
            'full_name', 
            'phone_number', 
            'role', 
            'created_at'
        ]
        read_only_fields = ['user_id', 'created_at']
    
    def validate_email(self, value):
        """Validate email uniqueness."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for Message model."""
    sender = UserSerializer(read_only=True)
    sender_id = serializers.UUIDField(write_only=True)
    sender_name = serializers.CharField(source='sender.username', read_only=True)
    
    class Meta:
        model = Message
        fields = [
            'message_id',
            'sender',
            'sender_id',
            'sender_name',
            'conversation',
            'message_body',
            'sent_at'
        ]
        read_only_fields = ['message_id', 'sent_at']
    
    def validate_message_body(self, value):
        """Validate message body is not empty."""
        if not value or not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")
        if len(value) > 1000:
            raise serializers.ValidationError("Message body cannot exceed 1000 characters.")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for Conversation model with nested messages and participants."""
    participants = UserSerializer(many=True, read_only=True)
    participant_ids = serializers.ListField(
        child=serializers.UUIDField(),
        write_only=True,
        required=False
    )
    messages = MessageSerializer(many=True, read_only=True)
    conversation_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    
    class Meta:
        model = Conversation
        fields = [
            'conversation_id',
            'participants',
            'participant_ids',
            'messages',
            'conversation_name',
            'created_at'
        ]
        read_only_fields = ['conversation_id', 'created_at']
    
    def validate_participant_ids(self, value):
        """Validate participant IDs exist and conversation has at least 2 participants."""
        if len(value) < 2:
            raise serializers.ValidationError("A conversation must have at least 2 participants.")
        
        existing_users = User.objects.filter(user_id__in=value)
        if len(existing_users) != len(value):
            raise serializers.ValidationError("One or more participant IDs are invalid.")
        
        return value
    
    def create(self, validated_data):
        """Create conversation with participants."""
        participant_ids = validated_data.pop('participant_ids', [])
        conversation = Conversation.objects.create(**validated_data)
        
        if participant_ids:
            participants = User.objects.filter(user_id__in=participant_ids)
            conversation.participants.set(participants)
        
        return conversation
    
    def update(self, instance, validated_data):
        """Update conversation and handle participants."""
        participant_ids = validated_data.pop('participant_ids', None)
        
        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update participants if provided
        if participant_ids is not None:
            participants = User.objects.filter(user_id__in=participant_ids)
            instance.participants.set(participants)
        
        return instance


class ConversationListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing conversations without full nested data."""
    participants = UserSerializer(many=True, read_only=True)
    message_count = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()
    participant_names = serializers.CharField(source='get_participant_names', read_only=True)
    
    class Meta:
        model = Conversation
        fields = [
            'conversation_id',
            'participants',
            'participant_names',
            'message_count',
            'last_message',
            'created_at'
        ]
        read_only_fields = ['conversation_id', 'created_at']
    
    def get_message_count(self, obj):
        """Get total number of messages in conversation."""
        return obj.messages.count()
    
    def get_last_message(self, obj):
        """Get the latest message in conversation."""
        last_message = obj.messages.order_by('-sent_at').first()
        if last_message:
            return {
                'message_body': last_message.message_body,
                'sender': last_message.sender.username,
                'sent_at': last_message.sent_at
            }
        return None


class MessageCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating messages."""
    
    class Meta:
        model = Message
        fields = [
            'conversation',
            'message_body'
        ]
    
    def validate_conversation(self, value):
        """Validate user is part of the conversation."""
        user = self.context['request'].user
        if not value.participants.filter(user_id=user.user_id).exists():
            raise serializers.ValidationError("You are not a participant in this conversation.")
        return value
    
    def validate_message_body(self, value):
        """Validate message body."""
        if not value or not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")
        return value
    
    def create(self, validated_data):
        """Create message with current user as sender."""
        validated_data['sender'] = self.context['request'].user
        return super().create(validated_data)