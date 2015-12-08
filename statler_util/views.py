import json  # Python builtin
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import JsonResponse, HttpResponse
from statler_api.models import PlayList, Play


def getDirectorsReport(request):
    all_plays = get_object_or_404(PlayList, url_title="all")
    return render(request, 'util/directors-report.html', {'all_plays': all_plays})

def getApprovalPage(request, play_id):
    """returns an html page which will facilitate approval of reviews"""

    return render(
        request,
        'util/review-approval-page.html',
        {'play': get_object_or_404(Play, url_title=play_id)})


def postApprovedReviews(request, play_id):
    """Accept the top reviews as JSON"""

    approved = json.loads(request.body.decode('utf-8'))

    play = get_object_or_404(Play, url_title=play_id)
    reviews = play.review_set
    reviews.update(top_review_rank=None)


    numApproved = 0

    if (approved):
        if approved["top-1"]:
            top1 = reviews.get(pk=approved["top-1"])
            top1.top_review_rank = 1
            top1.save()
            numApproved += 1

        if approved["top-2"]:
            top2 = reviews.get(pk=approved["top-2"])
            top2.top_review_rank = 2
            top2.save()
            numApproved += 1

        if approved["top-3"]:
            top3 = reviews.get(pk=approved["top-3"])
            top3.top_review_rank = 3
            top3.save()
            numApproved += 1
        
    return JsonResponse({ "message": "Success! " + str(numApproved) + " reviews approved." })
