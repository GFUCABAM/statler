from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<play_id>[^,/]+)/$', views.getApprovalPage, name='play-detail'),
]

