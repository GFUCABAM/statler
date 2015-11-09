from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
import json
from .models import *
from .api_models import *


def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""
    
    return HttpResponse("The API is alive.")


def getPlayList(request):
    """called when a GET request is sent to /api/play-list/
    returns json of the list of plays
    see https://docs.djangoproject.com/en/1.8/topics/serialization/"""
    #TODO: get an actual PlayList object instead of all plays

    aPlayDictList = [vars(Play(x)) for x in PlayDAO.objects.all()]

    # Remove reviews from each play dict, because we aren't going
    # that deep in the object graph
    for aPlayDict in aPlayDictList:
        del aPlayDict["reviews"]
        
    return HttpResponse(json.dumps(aPlayDictList))
    

def getPlayDetail(request, play_id):
    """called when a GET request is sent to /api/play/<play_id>
    returns json for the play"""
    
    play = vars(Play(get_object_or_404(PlayDAO, url_title=play_id)))

    # Convert reviews to dicts so they will serialize
    reviews = play["reviews"]
    for i in range(len(reviews)):
        reviews[i] = vars(reviews[i])
        # convert timestamps to iso strings so they will serialize
        reviews[i]["timestamp"] = reviews[i]["timestamp"].isoformat()
    
    return HttpResponse(json.dumps(play))
