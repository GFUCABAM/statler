from django.http import HttpResponse
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

    aPlayEntryList = PlayList(get_object_or_404(PlayListDAO, url_title=play_list_id)).entries

    aPlayEntryList = [vars(x) for x in aPlayEntryList]
    for aPlayEntry in aPlayEntryList:
        aPlayEntry["play"] = vars(aPlayEntry["play"])
        del aPlayEntry["play"]["reviews"]
    
    return HttpResponse(json.dumps(aPlayEntryList))
    

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
    incomingData = json.loads(request.body.decode('utf-8'))
    review = NewReview(play_id, html.escape(incomingData["text"]))
    review.toDao().save()

    reviewDict = vars(review)
    # convert timestamp to iso string so it will serialize
    reviewDict["timestamp"] = reviewDict["timestamp"].isoformat()
    # return the review object created
    return HttpResponse(json.dumps(reviewDict))
