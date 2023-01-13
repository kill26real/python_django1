from django.http import HttpRequest
from django.utils import timezone
from datetime import timedelta as td
from django.core.cache import cache


def setup_useragent_on_request_middleware(get_response):

    def middleware(request: HttpRequest):
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)

        return response

    return middleware


def trottling_middleware(get_response):

    def middleware(request: HttpRequest):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(',')[0]
        else:
            client_ip = request.META.get('REMOTE_ADDR')

        last_activity = cache.get_or_set(f'ip:{client_ip}', 0, 60)

        too_old_time = timezone.now() - td(seconds=60)
        if not last_activity or last_activity < too_old_time:
            response = get_response(request)
            return response
        else:
            raise Exception

    return middleware

class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        response = self.get_response(request)
        self.responses_count += 1
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1