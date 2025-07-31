"""
URL configuration for messaging_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return HttpResponse("""
    <h1>Django Middleware Project</h1>
    <p>Welcome to the Django Middleware demonstration project!</p>
    <h3>Available Endpoints:</h3>
    <ul>
        <li><a href="/admin/">Admin Panel</a></li>
        <li><a href="/api/">API Root</a></li>
        <li><a href="/api/token/">Get JWT Token</a></li>
        <li><a href="/api/users/">Users API</a></li>
        <li><a href="/api/conversations/">Conversations API</a></li>
        <li><a href="/api/messages/">Messages API</a></li>
    </ul>
    <p>Your middleware is working in the background!</p>
    <p>Check <code>requests.log</code> file for request logs.</p>
    """)

def home_view(request):
    """Home page view that renders the styled template"""
    return render(request, 'home.html')

urlpatterns = [
     path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),  # Include chat API routes with 'api/' prefix
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Add DRF auth URLs
]
