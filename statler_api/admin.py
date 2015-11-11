from django.contrib import admin
from .models import PlayDAO
from .models import ReviewDAO
from .models import PlayListDAO
from .models import PlayListEntryDAO

# show plays on the auto-generated admin site
admin.site.register(PlayDAO)
admin.site.register(ReviewDAO)
admin.site.register(PlayListDAO)
admin.site.register(PlayListEntryDAO)
