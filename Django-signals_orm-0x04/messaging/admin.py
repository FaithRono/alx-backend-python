from django.contrib import admin
from .models import Message, Notification, MessageHistory

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'content', 'timestamp', 'read', 'edited', 'edited_at']
    list_filter = ['read', 'edited', 'timestamp']
    search_fields = ['sender__username', 'receiver__username', 'content']
    readonly_fields = ['timestamp', 'edited_at']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'timestamp', 'is_read']
    list_filter = ['is_read', 'timestamp']
    search_fields = ['user__username']

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ['message', 'edited_by', 'edited_at', 'old_content']
    list_filter = ['edited_at']
    search_fields = ['message__content', 'old_content', 'edited_by__username']
    readonly_fields = ['edited_at']