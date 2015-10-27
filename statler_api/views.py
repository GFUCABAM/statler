from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from .models import Play

def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""
    return HttpResponse("The API is alive.")

def getPlayList(request):
    """called when a GET request is sent to /api/play-list/
    returns json of the list of plays
    see https://docs.djangoproject.com/en/1.8/topics/serialization/"""
    playList = Play.objects.all()
    #TODO: wrap playList in another object to control what fields are sent
    return HttpResponse(serializers.serialize("json", playList))

def getPlayDetail(request, play_id):
    """called when a GET request is sent to /api/play/<play_id>
    returns json for the play"""
    play = get_object_or_404(Play, url_title=play_id)
    #TODO: wrap play in another object to control what fields are sent
    return HttpResponse(serializers.serialize("json", [play]))
