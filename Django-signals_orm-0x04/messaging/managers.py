from django.db import models

class UnreadMessagesManager(models.Manager):
    """Custom manager to filter unread messages for a specific user"""
    
    def unread_for_user(self, user):
        """Get all unread messages for a specific user"""
        return self.filter(receiver=user, read=False).only(
            'id', 'sender__username', 'content', 'timestamp'
        ).select_related('sender')
    
    def mark_as_read(self, user, message_ids=None):
        """Mark messages as read for a user"""
        queryset = self.filter(receiver=user, read=False)
        if message_ids:
            queryset = queryset.filter(id__in=message_ids)
        return queryset.update(read=True)
    
    def get_queryset(self):
        """Return the base queryset"""
        return super().get_queryset()