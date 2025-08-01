from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inbox/', views.inbox, name='inbox'),
    path('unread/', views.unread_messages_view, name='unread_messages'),  # New URL
    path('conversation/<int:conversation_id>/', views.conversation, name='conversation'),
    path('threaded/<int:message_id>/', views.threaded_conversation, name='threaded_conversation'),
    path('send/', views.send_message, name='send_message'),
    path('edit/<int:message_id>/', views.edit_message, name='edit_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('history/<int:message_id>/', views.message_history, name='message_history'),
    path('mark-read/', views.mark_messages_read, name='mark_messages_read'),
    path('delete-account/', views.delete_user, name='delete_user'),
]