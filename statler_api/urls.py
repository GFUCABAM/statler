from django.conf.urls import url
from . import views

urlpatterns = [
    # urls that look like /api/play-list/ are forwarded to
    # the views.getPlayList function
    url(r'^play-list/$', views.getPlayList, name='play-list'),
]
