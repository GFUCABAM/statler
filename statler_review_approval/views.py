from django.shortcuts import render, render_to_response, get_object_or_404
from statler_api.models import PlayDAO


def getApprovalPage(request, play_id):
    """returns an html page which will facilitate approval of reviews"""

    return render(
        request,
        'statler_reveiew_approval/review-approval-page.html',
        {'playDAO': get_object_or_404(PlayDAO, url_title=play_id)})
