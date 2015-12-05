from django.contrib import admin
from .models import Play
from .models import Review
from .models import PlayList
from .models import PlayListEntry

# these 2 classes make it possible to add plays to a play list
# without manually making a PlayListEntry
class PlayListEntryInline(admin.TabularInline):
    model = PlayListEntry
    extra = 0


class PlayListAdmin(admin.ModelAdmin):
    inlines = [PlayListEntryInline]


# these 2 classes allow editing of reviews on the play admin page.
# see https://docs.djangoproject.com/en/1.8/intro/tutorial02/#adding-related-objects
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class PlayAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]

# the list of reviews will include fields for the play and top_review_rank
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'play', 'top_review_rank')
    list_editable = ('top_review_rank',)

# show plays on the auto-generated admin site
admin.site.register(Review, ReviewAdmin)
admin.site.register(Play, PlayAdmin)
admin.site.register(PlayList, PlayListAdmin)
