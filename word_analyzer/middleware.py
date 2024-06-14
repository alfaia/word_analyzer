from django.http import JsonResponse


class ContentTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.method == 'POST'
            and request.content_type != 'application/json'
        ):
            return JsonResponse(
                {'error': 'Content type must be application/json'}, status=415
            )
        return self.get_response(request)
