"""Data Access Objects, mapped to database tables.

These should be mapped to the api objects in api_models.py"""


from django.db import models


# Create your models here.
class PlayDAO(models.Model):
    """Represents a single performance in the database.

    The class/table contains static data regarding the performance. Data that will
    change over time will be store elsewhere."""

    # Note: these lengths are arbitrary.
    url_title = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    # null refers to database structure. blank refers to Django validation.
    actors = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    image = models.FileField(upload_to="static", blank=True, null=True)
    show_times = models.CharField(max_length=256, blank=True)

    def __str__(self):
        """default string representation"""

        return self.title


class ReviewDAO(models.Model):
    """Represents a review of a play."""

    play = models.ForeignKey(PlayDAO)
    text = models.TextField()
    rating = models.FloatField()
    timestamp = models.DateTimeField()

    # TODO Play rating ought to be dealt with at the database level. I'll leave it out for now.
    # play_rating = models.FloatField()

    def __str__(self):
        """default string representation: The first 16 characters of the review"""

        return self.text[:16]


class PlayListDAO(models.Model):
    """A persisted list of plays."""

    title = models.CharField(max_length=256)
    url_title = models.CharField(max_length=32)

    def __str__(self):
        """default string representation"""

        return self.title


class PlayListEntryDAO(models.Model):
    """Glues together Plays and PlayLists in an optionally ordered fashion."""

    play_list = models.ForeignKey(PlayListDAO)
    play = models.ForeignKey(PlayDAO)
    # Note that the order is optional.
    play_list_order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """default string representation"""

        return self.play.title + " in " + self.play_list.title
