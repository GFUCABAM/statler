from django.http import HttpResponse
from django.core import serializers
from .models import Play

#called when a GET request is sent to /plays/
#returns json of the list of plays
#see https://docs.djangoproject.com/en/1.8/topics/serialization/
def getPlayList(request):
    return HttpResponse(serializers.serialize("json", Play.objects.all()))
