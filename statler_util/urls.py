from django.conf.urls import url
# Reference the views contained in this app.
from . import views

# This is where the magical regex mapping happens.
urlpatterns = [
    # urls that look like 'util/directors-report/' are handled here
    # uncomment this line to test director's report page
    # comment this out to prevent the public from viewing the director's report page
    # TODO: put this behind admin authorization
    url(r'^directors-report/$', views.getDirectorsReport, name='directors-report')
]
