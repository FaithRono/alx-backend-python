from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.cache import cache_page
from .models import Message, Notification, MessageHistory

@login_required
def inbox(request):
    """Display inbox with received messages"""
    user = request.user
    # Use select_related and prefetch_related for optimization
    messages = Message.objects.filter(
        receiver=user
    ).select_related('sender').prefetch_related('replies').order_by('-timestamp')
    
    # Use the custom manager for unread messages
    unread_messages = Message.unread_objects.unread_for_user(user)
    
    return render(request, 'messaging/inbox.html', {
        'messages': messages, 
        'unread_messages': unread_messages
    })

@login_required
@cache_page(60)  # Cache for 60 seconds (Task 5)
def conversation(request, conversation_id):
    """Display conversation messages with threading"""
    user = request.user
    # Get messages for the conversation with optimization
    messages = Message.objects.filter(
        id=conversation_id
    ).select_related('sender').prefetch_related('replies__sender')
    
    # Get all replies recursively
    main_message = get_object_or_404(Message, id=conversation_id)
    replies = Message.objects.filter(
        parent_message=main_message
    ).select_related('sender').prefetch_related('replies')
    
    return render(request, 'messaging/conversation.html', {
        'main_message': main_message,
        'replies': replies
    })

@login_required
def delete_message(request, message_id):
    """Delete a specific message"""
    message = get_object_or_404(Message, id=message_id, receiver=request.user)
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message deleted successfully.')
        return redirect('inbox')
    return render(request, 'messaging/confirm_delete.html', {'message': message})

@login_required
def delete_user(request):
    """Allow a user to delete their account"""
    user = request.user
    
    if request.method == 'POST':
        # Confirm deletion
        confirmation = request.POST.get('confirm_delete')
        if confirmation == 'DELETE':
            # Log out the user first
            logout(request)
            # Delete the user (signals will handle cleanup)
            user.delete()
            messages.success(request, 'Your account has been deleted successfully.')
            return redirect('home')  # Redirect to home page or login
        else:
            messages.error(request, 'Please type DELETE to confirm account deletion.')
    
    return render(request, 'messaging/delete_user.html', {'user': user})

@login_required
def send_message(request):
    """Send a new message"""
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver_id')
        content = request.POST.get('content')
        parent_message_id = request.POST.get('parent_message_id')  # For replies
        
        try:
            from django.contrib.auth.models import User
            receiver = User.objects.get(id=receiver_id)
            
            # Create the message
            message = Message.objects.create(
                sender=request.user,
                receiver=receiver,
                content=content,
                parent_message=Message.objects.get(id=parent_message_id) if parent_message_id else None
            )
            
            messages.success(request, 'Message sent successfully.')
            return redirect('inbox')
            
        except User.DoesNotExist:
            messages.error(request, 'Receiver not found.')
        except Exception as e:
            messages.error(request, f'Error sending message: {str(e)}')
    
    from django.contrib.auth.models import User
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'messaging/send_message.html', {'users': users})

@login_required
def edit_message(request, message_id):
    """Edit a message (triggers pre_save signal for history)"""
    message = get_object_or_404(Message, id=message_id, sender=request.user)
    
    if request.method == 'POST':
        new_content = request.POST.get('content')
        if new_content and new_content != message.content:
            # Update the message (pre_save signal will handle history)
            message.content = new_content
            message.save()
            messages.success(request, 'Message updated successfully.')
            return redirect('inbox')
    
    return render(request, 'messaging/edit_message.html', {'message': message})

@login_required
def message_history(request, message_id):
    """View edit history of a message"""
    message = get_object_or_404(Message, id=message_id)
    
    # Check if user can view this message
    if message.sender != request.user and message.receiver != request.user:
        messages.error(request, 'You do not have permission to view this message history.')
        return redirect('inbox')
    
    # Get message history
    history = MessageHistory.objects.filter(message=message).order_by('-edited_at')
    
    return render(request, 'messaging/message_history.html', {
        'message': message,
        'history': history
    })

@login_required
def mark_messages_read(request):
    """Mark messages as read"""
    if request.method == 'POST':
        message_ids = request.POST.getlist('message_ids')
        if message_ids:
            Message.unread_objects.mark_as_read(request.user, message_ids)
            messages.success(request, 'Messages marked as read.')
    
    return redirect('inbox')

@login_required
def threaded_conversation(request, message_id):
    """Display threaded conversation using advanced ORM (Task 3)"""
    # Get the root message
    root_message = get_object_or_404(Message, id=message_id)
    
    # Use prefetch_related to optimize queries for replies
    messages_with_replies = Message.objects.filter(
        id=message_id
    ).prefetch_related(
        'replies__sender',
        'replies__replies__sender',  # For nested replies
        'replies__replies__replies__sender'  # For deeper nesting
    ).select_related('sender')
    
    return render(request, 'messaging/threaded_conversation.html', {
        'root_message': root_message,
        'messages': messages_with_replies
    })

def home(request):
    """Home page"""
    return render(request, 'messaging/home.html')