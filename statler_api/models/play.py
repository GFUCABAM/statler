from django.db import models


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
