from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.core import serializers
from django.utils import html
import json
from .models import *
from .api_models import *


def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""
    
    return HttpResponse("The API is alive.")


def getPlayList(request, play_list_id):
    """called when a GET request is sent to /api/play-list/
    returns json of the list of plays
    see https://docs.djangoproject.com/en/1.8/topics/serialization/"""

    if play_list_id == "all":
        # /api/play_lists/all/ will automatically return all plays
        aPlayList = PlayDAO.objects.all();
    else:
        aPlayList = get_object_or_404(PlayListDAO, url_title=play_list_id).plays.all()

    aPlayDictList = [vars(Play(x)) for x in aPlayList]

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


def postReview(request, play_id):
    """called when a POST request is sent to /api/play/<play_id>/reviews
    returns json for the review added"""

    # create and save a review
    # html.escape should prevent cross-site scripting attacks
    NewReview(play_id, html.escape(request.POST['text'])).toDao().save()

    # return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('play-detail', args=(play_id,)))
