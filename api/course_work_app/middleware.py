from django.http import JsonResponse
from course_work.settings import authorization_key as auth_key_default

class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the authorization key is present in the request headers
        authorization_key = request.headers.get('Authorization')
        if not authorization_key or authorization_key != auth_key_default:
            return JsonResponse({'error': 'Authorization key missing'}, status=401)
        return self.get_response(request)