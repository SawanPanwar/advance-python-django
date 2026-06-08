from django.http import HttpResponse


def test_sos(request):
    return HttpResponse('<h1>welcome to sos app</h1>')
