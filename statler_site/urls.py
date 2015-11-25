from django.conf.urls import url
# Reference this app's views.
from . import views

# This is where the magical regex mapping happens.
urlpatterns = [
    # urls that look like 'health-check/'
    url(r'^health-check/$', views.healthCheck, name='health-check'),

    # urls that look like 'play/<play_id>/'
    url(r'^play/(?P<play_id>[^,/]+)/$', views.getPlayDetailPage, name='play-detail'),

    # urls that look like 'play-list/<play_list_id>/'
    url(r'^play-list/(?P<play_list_id>[^,/]+)/$', views.getPlayListPage, name='play-list'),

    # blank urls are forwarded to the getLandingPage function
    url(r'^$', views.getLandingPage, name='play-list'),
]
