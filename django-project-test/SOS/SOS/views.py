from django.http import HttpResponse


def test_sos(request):
    return HttpResponse('<h1>Welcome to SOS Django Project</h1>')

