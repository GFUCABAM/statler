from django.shortcuts import render
from django.http import HttpResponse


def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""

    return HttpResponse("The site is alive.")


def index(request):
    """The Fake index
    TODO: Replace me!"""

    return HttpResponse("Fake index.")

