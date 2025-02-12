from django.http import HttpResponse


def test(request):
    return HttpResponse("<h1>Hello Django</h1>")