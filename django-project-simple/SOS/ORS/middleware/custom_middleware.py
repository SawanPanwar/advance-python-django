from django.http import HttpResponse


class SimpleMiddleware:
    count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        SimpleMiddleware.count += 1
        print("Middleware = ", SimpleMiddleware.count)
        res = self.get_response(request)
        # return HttpResponse("<center><h1>Welcome to Middleware</h1></center>")
        return res
