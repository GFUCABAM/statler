from django.contrib import admin
from django import forms
from .models import *

# these 2 classes make it possible to add plays to a play list
# without manually making a PlayListEntryDAO
class PlayListEntryInline(admin.TabularInline):
    model = PlayListEntryDAO
    extra = 0

class PlayListAdmin(admin.ModelAdmin):
    inlines = [PlayListEntryInline]

# these 2 classes allow editing of reviews on the play admin page.
# see https://docs.djangoproject.com/en/1.8/intro/tutorial02/#adding-related-objects
class ReviewInline(admin.TabularInline):
    model = ReviewDAO
    extra = 0

class PlayAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]

# show plays on the auto-generated admin site
admin.site.register(PlayDAO, PlayAdmin)
admin.site.register(PlayListDAO, PlayListAdmin)
