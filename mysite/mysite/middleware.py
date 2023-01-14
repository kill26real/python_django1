from django.http import HttpRequest
from datetime import timedelta as td
import datetime
import os


def setup_useragent_on_request_middleware(get_response):
    def middleware(request: HttpRequest):
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)

        return response

    return middleware


# def trottling_middleware(get_response):
#     def middleware(request: HttpRequest):
#
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             client_ip = x_forwarded_for.split(',')[0]
#         else:
#             client_ip = request.META.get('REMOTE_ADDR')
#
#         now_sec = datetime.datetime.now().timestamp()
#
#         last_activity = ''
#         if f'{client_ip}_last_request.txt' in os.listdir():
#             with open(f'{client_ip}_last_request.txt', 'r') as file:
#                 last_activity = file.read()
#                 print(last_activity)
#         else:
#             with open(f'{client_ip}_last_request.txt', 'w') as file:
#                 file.write(str(now_sec))
#
#         response = get_response(request)
#
#         too_old_time = now_sec - 30
#         if not last_activity or float(last_activity) < too_old_time:
#             with open(f'{client_ip}_last_request.txt', 'w') as file:
#                 file.write(str(now_sec))
#             return response
#         else:
#             raise PermissionError
#
#     return middleware


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
