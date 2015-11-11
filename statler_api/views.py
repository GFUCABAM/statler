from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .statler_json import serializeModel
from .api_models import *


def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""
    
    return HttpResponse("The API is alive.")


def getPlayList(request):
    """called when a GET request is sent to /api/play-list/
    returns json of the list of plays
    see https://docs.djangoproject.com/en/1.8/topics/serialization/"""

    # TODO: dynamically get an actual PlayList object instead of hardcoded "all"
    aPlayList = get_object_or_404(PlayListDAO, url_title="all")
    return HttpResponse(serializeModel(aPlayList), content_type="application/json")
    

def getPlayDetail(request, play_id):
    """called when a GET request is sent to /api/play/<play_id>
    returns json for the play"""
    
    play = get_object_or_404(PlayDAO, url_title=play_id)

    return HttpResponse(serializeModel(play), content_type="application/json")
