from django.shortcuts import render
from django.http import HttpResponse

def healthCheck(request):
    """Returns a string. This shouldn't break. We can use this
    to confirm the server is on its feet."""
    return HttpResponse("The site is alive.")

def getPlayListPage(request, play_list_id):
    """returns an html page which will use JavaScript
    to get and display data"""
    return render(request, 'play-list-page.html', {'play_list_id': play_list_id})

def getPlayDetailPage(request, play_id):
    """returns an html page which will use JavaScript
    to get and display data"""
    return render(request, 'play-detail-page.html', {'play_id': play_id})

def getLandingPage(request):
    """returns an html page which will use JavaScript
    to get and display data"""
    return render(request, 'landing-page.html', {})
