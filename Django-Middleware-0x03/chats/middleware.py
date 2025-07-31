import logging
from datetime import datetime
from django.http import HttpResponseForbidden, HttpResponseTooManyRequests
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.utils import timezone

# Configure logging for requests
logging.basicConfig(
    filename='requests.log',
    level=logging.INFO,
    format='%(message)s'
)

class RequestLoggingMiddleware(MiddlewareMixin):
    """
    Middleware to log each user's requests to a file.
    Logs timestamp, user, and request path.
    """
    
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__(get_response)

    def __call__(self, request):
        # Get user info
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        
        # Log the request
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)
        
        # Continue with the request
        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware(MiddlewareMixin):
    """
    Middleware to restrict access to messaging app during certain hours.
    Blocks access outside 9 AM to 6 PM.
    """
    
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__(get_response)

    def __call__(self, request):
        current_hour = timezone.now().hour
        
        # Check if accessing chat-related paths
        if '/api/messages/' in request.path or '/api/conversations/' in request.path:
            # Block access outside 9 AM (9) to 6 PM (18)
            if current_hour < 9 or current_hour >= 18:
                return HttpResponseForbidden("Chat access is restricted during these hours (6 PM - 9 AM)")
        
        response = self.get_response(request)
        return response


class OffensiveLanguageMiddleware(MiddlewareMixin):
    """
    Middleware to limit the number of chat messages a user can send.
    Implements rate limiting: 5 messages per minute per IP address.
    """
    
    def __init__(self, get_response=None):
        self.get_response = get_response
        self.max_requests = 5
        self.time_window = 60  # 1 minute in seconds
        super().__init__(get_response)

    def __call__(self, request):
        # Only apply to POST requests on message endpoints
        if request.method == 'POST' and '/api/messages/' in request.path:
            ip_address = self.get_client_ip(request)
            cache_key = f"rate_limit_{ip_address}"
            
            # Get current request count for this IP
            request_data = cache.get(cache_key, {'count': 0, 'timestamp': timezone.now()})
            
            # Check if time window has passed
            time_diff = (timezone.now() - request_data['timestamp']).total_seconds()
            if time_diff > self.time_window:
                request_data = {'count': 1, 'timestamp': timezone.now()}
            else:
                request_data['count'] += 1
            
            # Check if limit exceeded
            if request_data['count'] > self.max_requests:
                return HttpResponseTooManyRequests("Rate limit exceeded. You can only send 5 messages per minute.")
            
            # Update cache
            cache.set(cache_key, request_data, self.time_window)
        
        response = self.get_response(request)
        return response
    
    def get_client_ip(self, request):
        """Get the client's IP address from request."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class RolePermissionMiddleware(MiddlewareMixin):
    """
    Middleware to check user roles before allowing access to specific actions.
    Restricts certain endpoints to admin or moderator roles only.
    """
    
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__(get_response)

    def __call__(self, request):
        # Define protected paths that require admin/moderator access
        protected_paths = ['/api/users/', '/admin/']
        
        # Check if the current path needs role-based protection
        if any(path in request.path for path in protected_paths):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Authentication required")
            
            # Check if user has the required role
            user_role = getattr(request.user, 'role', None)
            if user_role not in ['admin', 'moderator']:
                return HttpResponseForbidden("Insufficient permissions. Admin or moderator role required.")
        
        response = self.get_response(request)
        return response