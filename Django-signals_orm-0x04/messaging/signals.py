from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

# Signal to create a notification when a new message is received
@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance,
            content=f"You have received a new message from {instance.sender.username}: {instance.content}",
            timestamp=instance.timestamp
        )

# Signal to log the old content of a message before it is edited
@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Check if the message already exists
        old_message = Message.objects.get(pk=instance.pk)
        MessageHistory.objects.create(
            message=old_message,
            old_content=old_message.content,
            edited_at=old_message.timestamp
        )

# Signal to delete related data when a user account is deleted
@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    Message.objects.filter(receiver=instance).delete()
    Notification.objects.filter(user=instance).delete()
    MessageHistory.objects.filter(message__sender=instance).delete()