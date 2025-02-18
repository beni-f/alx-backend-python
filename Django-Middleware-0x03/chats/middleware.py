import logging
from datetime import datetime
from django.http import HttpResponseForbidden

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