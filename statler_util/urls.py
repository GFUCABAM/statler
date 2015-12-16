from django.conf.urls import url
# Reference the views contained in this app.
from . import views

# This is where the magical regex mapping happens.
urlpatterns = [
    url(r'^report/$', views.getSimplePlayIndex, name='report-index'),
    url(r'^report/(?P<play_id>[^,/]+)/$', views.getDirectorsReport, name='report'),

    url(r'^approve/$', views.getSimplePlayIndex, name='approve-index'),
    url(r'^approve/(?P<play_id>[^,/]+)/$', views.getApprovalPage, name='approve'),
    url(r'^approved/(?P<play_id>[^,/]+)/reviews/$', views.postApprovedReviews, name='approved-reviews'),
]
