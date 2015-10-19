from django.conf.urls import url
# Reference the views contained in this app.
from . import views

# This is where the magical regex mapping happens.
urlpatterns = [
    # urls that look like /api/health-check/ are forwarded to
    # the views.healthCheck function
    url(r'^health-check/$', views.healthCheck, name='health-check'),
    
    # urls that look like /api/play-list/ are forwarded to
    # the views.getPlayList function
    url(r'^play-list/$', views.getPlayList, name='play-list'),
]
