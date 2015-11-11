from django.contrib import admin
from .models import Play
from .models import Review
from .models import PlayList
from .models import PlayListEntry

# show plays on the auto-generated admin site
admin.site.register(Play)
admin.site.register(Review)
admin.site.register(PlayList)
admin.site.register(PlayListEntry)
