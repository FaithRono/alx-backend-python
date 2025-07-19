from django.contrib import admin
from .models import User, Conversation, Message

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'created_at']
    list_filter = ['role', 'created_at']
    search_fields = ['username', 'email']

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
    filter_horizontal = ['participants']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'conversation', 'sent_at']
    list_filter = ['sent_at']
    search_fields = ['message_body', 'sender__username']
# Register your models here.
