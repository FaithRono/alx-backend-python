from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

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

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),
]