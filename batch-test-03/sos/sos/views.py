from django.http import HttpResponse


def test_sos(request):
    return HttpResponse('<h1>This is  my SOS Django Project</h1>')


def test_hello(request):
    return HttpResponse('<h1>This is Hello Function</h1>')
