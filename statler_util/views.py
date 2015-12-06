from django.shortcuts import get_object_or_404, render

from statler_api.models import PlayList


def getDirectorsReport(request):
    all_plays = get_object_or_404(PlayList, url_title="all")
    return render(request, 'directors-report.html', {'all_plays': all_plays})
