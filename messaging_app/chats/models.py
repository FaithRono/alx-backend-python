import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# ===============================
# 1. User Model
# ===============================
class User(AbstractUser):
    """Custom user model extending Django's AbstractUser."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    class Roles(models.TextChoices):
        GUEST = 'guest', 'Guest'
        HOST = 'host', 'Host'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.GUEST)
    created_at = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    USERNAME_FIELD = 'username'

    def _str_(self):
        return f"{self.username} ({self.role})"


# ===============================
# 2. Conversation Model
# ===============================
class Conversation(models.Model):
    """Conversation model containing multiple participants."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return f"Conversation {self.id}"


# ===============================
# 3. Message Model
# ===============================
class Message(models.Model):
    """Message model storing text messages sent by users."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return f"Message from {self.sender.username} at {self.sent_at}"