import logging
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def __call__(self, request, *args, **kwds):
        user = request.user if request.user.is_authenticated else "Anon"
        self.logger.info(f"{datetime.now()} - User:{user} - Path:{request.path}")
        response = self.get_response(request)
        return response