from django.conf.urls import url
# Reference this app's views.
from . import views

# This is where the magical regex mapping happens.
urlpatterns = [
    # urls that look like 'health-check/'
    url(r'^health-check/$', views.healthCheck, name='health-check'),

    # urls that look like 'play/<play_id>/'
    url(r'^play/(?P<play_id>[^,/]+)/$', views.getPlayDetailPage, name='play-detail'),
    
    # blank urls are forwarded to
    # the views.getPlayListPage function
    url(r'^$', views.getPlayListPage, name='play-list'),
]
