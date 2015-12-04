from django.conf.urls import url
# Reference the views contained in this app.
from . import views

# This is where the magical regex mapping happens.
urlpatterns = [
    # urls that look like /api/health-check/ are forwarded to
    # the views.healthCheck function
    url(r'^health-check/$', views.healthCheck, name='health-check'),

    # urls that look like /api/play/<play_id>/ are forwarded to
    # the views.getPlayDetail function
    url(r'^play/(?P<play_id>[^,/]+)/$', views.getPlayDetail, name='play-detail'),
    
    # urls that look like /api/play-list/<play_list_id> are forwarded to
    # the views.getPlayList function
    url(r'^play-list/(?P<play_list_id>[^,/]+)/$', views.getPlayList, name='play-list'),

    # posts to /api/play/<play_id>/reviews/ are handled here
    url(r'^play/(?P<play_id>[^,/]+)/reviews/$', views.postReview, name='play-reviews'),

    # urls that look like 'directors-report/' are handled here
    # uncomment this line to test director's report page
    # comment this out to prevent the public from viewing the director's report page
    # TODO: put this behind admin authorization
    url(r'^directors-report/$', views.getDirectorsReport, name='directors-report')
]
