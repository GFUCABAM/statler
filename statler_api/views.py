import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import html

from .statler_json import serializeModel
from .models import Play, PlayList, Review


def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""
    
    return HttpResponse("The API is alive.")


def getPlayList(request, play_list_id):
    """called when a GET request is sent to /api/play-list/
    returns json of the list of plays
    see https://docs.djangoproject.com/en/1.8/topics/serialization/"""

    playList = get_object_or_404(PlayList, url_title=play_list_id)
    return HttpResponse(serializeModel(playList), content_type="application/json")
    

def getPlayDetail(request, play_id):
    """called when a GET request is sent to /api/play/<play_id>
    returns json for the play"""
    
    play = get_object_or_404(Play, url_title=play_id)
    return HttpResponse(serializeModel(play), content_type="application/json")


def postReview(request, play_id):
    """called when a POST request is sent to /api/play/<play_id>/reviews
    returns json for the review added"""

    # html.escape should prevent cross-site scripting attacks
    incomingData = json.loads(request.body.decode('utf-8'))
    reviewText = html.escape(incomingData["text"])

    # Creates and saves a review.
    review = Review.createFromText(reviewText, play_id)

    # return the review object created. 201 status code denotes "created"
    return HttpResponse(serializeModel(review), content_type="application/json", status=201)
