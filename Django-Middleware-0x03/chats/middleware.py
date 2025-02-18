import logging
from datetime import datetime, timedelta
from django.http import HttpResponseForbidden
from collections import defaultdict

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)
        handler = logging.FileHandler(filename='requests.log')
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def __call__(self, request, *args, **kwds):
        user = request.user if request.user.is_authenticated else "Anon"
        self.logger.info(f"{datetime.now()} - User:{user} - Path:{request.path}")
        response = self.get_response(request)
        return response
    
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):
        response = self.get_response(request)
        current_hour = datetime.now().hour
        if (current_hour < 9 and current_hour > 18):
            return response
        else:
            return HttpResponseForbidden("Access restricted at this time of the day")
        
class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_count = defaultdict(list)

    def __call__(self, request, *args, **kwds):
        ip_address = request.META.get('REMOTE_ADDR')
        current_time = datetime.now()

        if request.path == '/api/message/' and request.method == 'POST':
            self.message_count[ip_address] = [time for time in self.message_count[ip_address] if current_time - time < timedelta(minutes=1)]

            if len(self.message_count[ip_address]) >= 5:
                return HttpResponseForbidden("You have exceeded the message limit")

            self.message_count[ip_address].append(current_time)

        response = self.get_response(request)
        return response
    
class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request, *args, **kwds):
        user = request.user
        if not user.is_staff:
            return HttpResponseForbidden("Can't access this page")
        response = self.get_response(request)
        return response