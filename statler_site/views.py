from django.shortcuts import render
from django.http import HttpResponse

def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""
    return HttpResponse("The site is alive.")

def getPlayListPage(request):
    """returns an html page which will use JavaScript
    to get and display data"""

    # 'all'  is the hardcoded play list name for getting all plays
    return render(request, 'play-list-page.html', {'play_list_id': 'all'})

def getPlayDetailPage(request, play_id):
    """returns an html page which will use JavaScript
    to get and display data"""
    return render(request, 'statler_site/play-detail-page.html', {'play_id': play_id})
