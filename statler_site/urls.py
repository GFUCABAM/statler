from django.conf.urls import url

# Reference this app's views. I believe our pages should be views.
from . import views

# This is where the magical regex mapping happens.
urlpatterns = [
    url(r'^health-check$', views.healthCheck, name='healthCheck'),

    # TODO: Replace this with the real index:
    url(r'^$', views.index, name='index'),
]