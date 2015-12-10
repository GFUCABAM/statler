import json  # Python builtin
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from statler_api.models import PlayList, Play

@login_required(login_url="/admin/login/")
def getDirectorsReport(request):
    all_plays = get_object_or_404(PlayList, url_title="all")
    return render(request, 'util/directors-report.html', {'all_plays': all_plays})

@login_required(login_url="/admin/login/")
def getApprovalPage(request, play_id):
    """returns an html page which will facilitate approval of reviews"""

    play = get_object_or_404(Play, url_title=play_id)
    alreadyTop = list(play.review_set.filter(top_review_rank__isnull=False).order_by("top_review_rank"))


    return render(
        request,
        'util/review-approval-page.html',
        {
            'play': play,
            'top1': alreadyTop[0] if len(alreadyTop) > 0 else None,
            'top2': alreadyTop[1] if len(alreadyTop) > 1 else None,
            'top3': alreadyTop[2] if len(alreadyTop) > 2 else None,
})


@login_required(login_url="/admin/login/")
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
