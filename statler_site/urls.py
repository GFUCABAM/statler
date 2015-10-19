from django.conf.urls import url
# Reference this app's views.
from . import views

# This is where the magical regex mapping happens.
urlpatterns = [
    url(r'^health-check/$', views.healthCheck, name='health-check'),
    
    # blank urls are forwarded to
    # the views.getPlayListPage function
    url(r'^$', views.getPlayListPage, name='play-list'),
]
