from django.contrib import admin
from .models import Message, Notification

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'content', 'read')
    search_fields = ('sender__username', 'receiver__username', 'content')
    list_filter = ('timestamp', 'read')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')
    search_fields = ('user__username', 'message__content')
    list_filter = ('created_at', 'is_read')