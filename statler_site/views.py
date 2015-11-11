from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""
    return HttpResponse("The site is alive.")

def getPlayListPage(request):
    """returns an html page which will use JavaScript
    to get and display data"""
    return render_to_response('play-list-page.html')

def getPlayDetailPage(request, play_id):
    """returns an html page which will use JavaScript
    to get and display data"""
    return render(request, 'play-detail-page.html', {'play_id': play_id})
