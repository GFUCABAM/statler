from django.conf.urls import url
from . import views

urlpatterns = [
    # urls that look like /plays/ are forwarded to
    # the views.getPlayListPage function
    url(r'^$', views.getPlayListPage, name='play-list'),
]
