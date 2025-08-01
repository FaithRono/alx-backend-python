from django.db import models
from django.contrib.auth.models import User

# Custom Manager for unread messages (Task 4)
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

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)
    edited_by = models.ForeignKey(User, null=True, blank=True, related_name='edited_messages', on_delete=models.SET_NULL)
    parent_message = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    # Add the custom manager
    objects = models.Manager()  # Default manager
    unread = UnreadMessagesManager()  # Custom manager for unread messages

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver} at {self.timestamp}'

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='notifications', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user} regarding message {self.message.id}'

class MessageHistory(models.Model):
    """Model to store message edit history"""
    message = models.ForeignKey(Message, related_name='history', on_delete=models.CASCADE)
    old_content = models.TextField()
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    edited_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-edited_at']
        verbose_name_plural = "Message histories"
    
    def __str__(self):
        return f'History for message {self.message.id} edited at {self.edited_at}'