from django.contrib import admin
from .models import Play

# show plays on the auto-generated admin site
admin.site.register(Play)
