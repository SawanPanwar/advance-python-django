from django.shortcuts import render

from django.http import HttpResponse


def test_ors(request):
    return HttpResponse('<h1>Welcome to ORS App</h1>')
