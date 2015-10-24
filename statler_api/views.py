from django.http import HttpResponse
from django.core import serializers
from .models import PlayDAO

def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""

    return HttpResponse("The API is alive.")

def getPlayList(request):
    """called when a GET request is sent to /api/play-list/
    returns json of the list of plays
    see https://docs.djangoproject.com/en/1.8/topics/serialization/"""
    
    return HttpResponse(serializers.serialize("json", PlayDAO.objects.all()))
