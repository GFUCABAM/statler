from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""

    return HttpResponse("The site is alive.")


def getPlayListPage(request):
    """returns a static html page which will use a script
    to get and display data"""
    
    return render_to_response('play-list-page.html')
