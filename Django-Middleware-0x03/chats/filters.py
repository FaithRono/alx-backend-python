import django_filters
from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Message, Conversation, User


class MessageFilter(django_filters.FilterSet):
    """Filter class for Message model."""
    
    # Date range filtering
    sent_after = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr='gte')
    sent_before = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr='lte')
    sent_date = django_filters.DateFilter(field_name="sent_at", lookup_expr='date')
    
    # Conversation filtering
    conversation = django_filters.UUIDFilter(field_name="conversation__conversation_id")
    
    # Sender filtering
    sender = django_filters.UUIDFilter(field_name="sender__user_id")
    sender_username = django_filters.CharFilter(field_name="sender__username", lookup_expr='icontains')
    
    # Message content filtering
    message_body = django_filters.CharFilter(field_name="message_body", lookup_expr='icontains')
    
    # Custom filter for messages with specific users
    with_user = django_filters.UUIDFilter(method='filter_with_user')
    
    # Time range filtering (last hour, day, week)
    time_range = django_filters.ChoiceFilter(
        choices=[
            ('hour', 'Last Hour'),
            ('day', 'Last Day'),
            ('week', 'Last Week'),
            ('month', 'Last Month'),
        ],
        method='filter_time_range'
    )
    
    class Meta:
        model = Message
        fields = {
            'sent_at': ['exact', 'gte', 'lte', 'date'],
            'conversation': ['exact'],
            'sender': ['exact'],
        }
    
    def filter_with_user(self, queryset, name, value):
        """Filter messages in conversations that include a specific user."""
        if value:
            user_conversations = Conversation.objects.filter(
                participants__user_id=value
            ).values_list('conversation_id', flat=True)
            
            return queryset.filter(conversation__conversation_id__in=user_conversations)
        return queryset
    
    def filter_time_range(self, queryset, name, value):
        """Filter messages by time range."""
        from django.utils import timezone
        from datetime import timedelta
        
        now = timezone.now()
        
        if value == 'hour':
            time_threshold = now - timedelta(hours=1)
        elif value == 'day':
            time_threshold = now - timedelta(days=1)
        elif value == 'week':
            time_threshold = now - timedelta(weeks=1)
        elif value == 'month':
            time_threshold = now - timedelta(days=30)
        else:
            return queryset
        
        return queryset.filter(sent_at__gte=time_threshold)


class ConversationFilter(django_filters.FilterSet):
    """Filter class for Conversation model."""
    
    # Date filtering
    created_after = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='gte')
    created_before = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='lte')
    
    # Participant filtering
    participant = django_filters.UUIDFilter(field_name="participants__user_id")
    participant_username = django_filters.CharFilter(field_name="participants__username", lookup_expr='icontains')
    
    # Custom filters
    has_messages = django_filters.BooleanFilter(method='filter_has_messages')
    participant_count = django_filters.NumberFilter(method='filter_participant_count')
    
    class Meta:
        model = Conversation
        fields = {
            'created_at': ['exact', 'gte', 'lte'],
            'participants': ['exact'],
        }
    
    def filter_has_messages(self, queryset, name, value):
        """Filter conversations that have messages."""
        if value is True:
            return queryset.filter(messages__isnull=False).distinct()
        elif value is False:
            return queryset.filter(messages__isnull=True).distinct()
        return queryset
    
    def filter_participant_count(self, queryset, name, value):
        """Filter conversations by number of participants."""
        from django.db.models import Count
        return queryset.annotate(
            participant_count=Count('participants')
        ).filter(participant_count=value)


class UserFilter(django_filters.FilterSet):
    """Filter class for User model."""
    
    # Basic filtering
    username = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    
    # Role filtering
    role = django_filters.ChoiceFilter(choices=User.Roles.choices)
    
    # Date filtering
    joined_after = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='gte')
    joined_before = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='lte')
    
    # Custom filters
    has_conversations = django_filters.BooleanFilter(method='filter_has_conversations')
    has_sent_messages = django_filters.BooleanFilter(method='filter_has_sent_messages')
    
    class Meta:
        model = User
        fields = {
            'username': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'role': ['exact'],
            'created_at': ['exact', 'gte', 'lte'],
        }
    
    def filter_has_conversations(self, queryset, name, value):
        """Filter users who have conversations."""
        if value is True:
            return queryset.filter(conversations__isnull=False).distinct()
        elif value is False:
            return queryset.filter(conversations__isnull=True).distinct()
        return queryset
    
    def filter_has_sent_messages(self, queryset, name, value):
        """Filter users who have sent messages."""
        if value is True:
            return queryset.filter(sent_messages__isnull=False).distinct()
        elif value is False:
            return queryset.filter(sent_messages__isnull=True).distinct()
        return queryset