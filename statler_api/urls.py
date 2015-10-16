from django.conf.urls import url

# Reference the views contained in this app. Will the API actually use views?
from . import views

# This is where the magical regex mapping happens.
urlpatterns = [
    url(r'^health-check$', views.healthCheck, name='healthCheck'),
]