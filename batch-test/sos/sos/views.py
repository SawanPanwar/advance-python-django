from django.http import HttpResponse


def test_sos(request):
    return HttpResponse("<h1>Django Project sos</h1>")