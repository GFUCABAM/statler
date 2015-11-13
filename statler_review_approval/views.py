import json  # Python builtin
from django.shortcuts import render, render_to_response, get_object_or_404
from statler_api.models import Play


def getApprovalPage(request, play_id):
    """returns an html page which will facilitate approval of reviews"""

    return render(
        request,
        'statler_reveiew_approval/review-approval-page.html',
        {'Play': get_object_or_404(Play, url_title=play_id)})


def setTopReviews(request, play_id):
    """Accept the top reviews as JSON"""

    json.deserialize(request.data);