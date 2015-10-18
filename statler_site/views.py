from django.shortcuts import render_to_response

#called when a GET request is sent to /plays/
#returns a static html page
def getPlayListPage(request):
    return render_to_response('play-list-page.html')
