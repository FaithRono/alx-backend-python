# Django REST Framework Messaging App Documentation

## Project Overview

We have built a comprehensive messaging application using Django and Django REST Framework. This application allows users to create conversations, send messages, and manage participants in a chat-like system.

---

## 1. Project Structure

```
messaging_app/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .gitignore
├── messaging_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── chats/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    └── migrations/
```

---

## 2. Database Models (`chats/models.py`)

### User Model
- **Extends Django's AbstractUser** to create a custom user model
- **Primary Key**: `user_id` (UUID field for better security)
- **Fields**:
  - `email` (unique)
  - `phone_number` (optional)
  - `role` (Guest, Host, Admin)
  - `created_at`
- **Purpose**: Manages user authentication and profiles

### Conversation Model
- **Primary Key**: `conversation_id` (UUID)
- **Relationships**: Many-to-many with User (participants)
- **Fields**:
  - `participants` (ManyToManyField to User)
  - `created_at`
- **Purpose**: Groups users together for messaging

### Message Model
- **Primary Key**: `message_id` (UUID)
- **Relationships**: 
  - Foreign key to User (sender)
  - Foreign key to Conversation
- **Fields**:
  - `message_body` (text content)
  - `sent_at` (timestamp)
- **Purpose**: Stores individual messages within conversations

---

## 3. API Serializers (`chats/serializers.py`)

### UserSerializer
- Serializes user data for API responses
- Includes validation for email uniqueness
- Excludes sensitive fields like password

### MessageSerializer
- Handles message data with nested sender information
- Includes validation for message content
- Supports both read and write operations

### ConversationSerializer
- **Full serializer** with nested participants and messages
- Handles participant management (add/remove)
- Custom create/update methods for complex relationships

### ConversationListSerializer
- **Optimized for listing** conversations
- Includes computed fields like message count
- Shows last message preview

### MessageCreateSerializer
- **Simplified for message creation**
- Validates user permissions for conversation participation
- Automatically sets current user as sender

---

## 4. API Views (`chats/views.py`)

### UserViewSet
- **CRUD operations** for user management
- **Role-based permissions** (admins see all, users see self)
- **Filtering/searching** by role, username, email

### ConversationViewSet
- **CRUD operations** for conversations
- **Custom actions**:
  - `add_participant` - Add user to conversation
  - `remove_participant` - Remove user from conversation
  - `messages` - Get all messages in conversation
- **Security**: Users only see conversations they participate in

### MessageViewSet
- **CRUD operations** for messages
- **Custom actions**:
  - `by_conversation` - Filter messages by conversation
  - `mark_as_read` - Mark message as read (placeholder)
- **Security**: Users can only edit/delete their own messages

### ConversationMessagesViewSet
- **Specialized view** for nested routing
- Gets messages within a specific conversation
- Read-only operations with proper permission checking

---

## 5. URL Routing (urls.py & urls.py)

### DefaultRouter
- Automatically creates standard CRUD endpoints:
  - `GET/POST /api/users/`
  - `GET/POST /api/conversations/`
  - `GET/POST /api/messages/`
  - `GET/PUT/PATCH/DELETE /api/{resource}/{id}/`

### NestedDefaultRouter
- Creates nested URLs for related resources:
  - `GET/POST /api/conversations/{id}/messages/`

### Main Project URLs
- **Admin interface**: `/admin/`
- **API endpoints**: `/api/` (includes all chat functionality)
- **Authentication**: `/api-auth/` (DRF browsable API login)

---

## 6. Django Admin Configuration (`chats/admin.py`)

### Custom Admin Classes
- **UserAdmin**: Shows user details, role, creation date
- **ConversationAdmin**: Lists conversations with participants
- **MessageAdmin**: Shows messages with sender and timestamp
- **Filtering and searching** capabilities for easy management

---

## 7. Settings Configuration (`messaging_app/settings.py`)

### Key Configurations
```python
# Custom User Model
AUTH_USER_MODEL = 'chats.User'

# REST Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'chats',
]
```

---

## 8. API Endpoints Summary

### Authentication Required for All Endpoints

#### Users
- `GET /api/users/` - List users
- `POST /api/users/` - Create user
- `GET /api/users/{user_id}/` - Get user details

#### Conversations
- `GET /api/conversations/` - List user's conversations
- `POST /api/conversations/` - Create new conversation
- `GET /api/conversations/{id}/` - Get conversation details
- `POST /api/conversations/{id}/add_participant/` - Add participant
- `POST /api/conversations/{id}/remove_participant/` - Remove participant

#### Messages
- `GET /api/messages/` - List user's messages
- `POST /api/messages/` - Send message to existing conversation
- `GET /api/messages/{id}/` - Get message details
- `GET /api/conversations/{id}/messages/` - Get conversation messages

---

## 9. Security Features

### Authentication & Authorization
- **Session authentication** for web interface
- **Token authentication** for API clients
- **Permission-based access** (users only see their data)
- **Role-based permissions** for admin functions

### Data Validation
- **Email uniqueness** validation
- **Message content** validation
- **Conversation participation** validation
- **UUID primary keys** for better security

---

## 10. Development Workflow Completed

### Setup Steps
1. ✅ Created Django project and app
2. ✅ Configured custom User model
3. ✅ Built database models with relationships
4. ✅ Created comprehensive serializers
5. ✅ Implemented ViewSets with custom actions
6. ✅ Configured URL routing with nested routes
7. ✅ Set up admin interface
8. ✅ Configured REST Framework settings
9. ✅ Created and applied migrations
10. ✅ Set up authentication system

### Key Features Achieved
- **Full CRUD operations** for all models
- **Nested relationships** properly handled
- **Real-time messaging capability** foundation
- **Admin interface** for management
- **API documentation** through DRF browsable API
- **Filtering and searching** capabilities
- **Proper error handling** and validation

---

## 11. Testing the Application

### Running the Server
```bash
python manage.py runserver
```

### Accessing the Application
- **API Root**: `http://127.0.0.1:8000/api/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **API Authentication**: `http://127.0.0.1:8000/api-auth/`

### Sample API Usage
1. **Create a conversation** with participants
2. **Send messages** to the conversation
3. **Add/remove participants** as needed
4. **List conversations** and messages
5. **Filter and search** through data

---

## 12. Technologies Used

- **Django 5.2** - Web framework
- **Django REST Framework** - API framework
- **SQLite** - Database (development)
- **UUID fields** - Primary keys for security
- **Token authentication** - API security
- **django-filter** - API filtering
- **drf-nested-routers** - Nested URL routing

This messaging application provides a solid foundation for a chat system with proper authentication, authorization, and RESTful API design following Django best practices.