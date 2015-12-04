﻿"""
Definition of urls for statler.
"""

from datetime import datetime
from django.conf.urls import patterns, url

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^api/', include('statler_api.urls', namespace="api")),
    url(r'^admin/', include(admin.site.urls)),
    
    # Default to statler_site
    url(r'^', include('statler_site.urls', namespace="site")),
]