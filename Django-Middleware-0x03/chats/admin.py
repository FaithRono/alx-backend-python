from django.contrib import admin
from .models import User, Conversation, Message

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['conversation_id', 'created_at']  # Change 'id' to 'conversation_id'
    list_filter = ['created_at']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'sender', 'conversation', 'sent_at']  # Use 'message_id' instead of 'id'
    list_filter = ['sent_at']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'email', 'role', 'created_at']  # Use 'user_id' instead of 'id'
    list_filter = ['role', 'created_at']