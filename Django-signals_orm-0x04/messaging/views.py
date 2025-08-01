from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message, Notification
from .managers import UnreadMessagesManager

@login_required
def inbox(request):
    user = request.user
    messages = Message.objects.filter(receiver=user).select_related('sender').prefetch_related('replies')
    unread_messages = UnreadMessagesManager().get_unread_messages(user)
    return render(request, 'messaging/inbox.html', {'messages': messages, 'unread_messages': unread_messages})

@login_required
def conversation(request, conversation_id):
    user = request.user
    messages = Message.objects.filter(conversation_id=conversation_id).select_related('sender').prefetch_related('replies')
    return render(request, 'messaging/conversation.html', {'messages': messages})

@login_required
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id, receiver=request.user)
    if request.method == 'POST':
        message.delete()
        return redirect('inbox')
    return render(request, 'messaging/confirm_delete.html', {'message': message})