from django.db import models

from statler_api.models import StatlerModel


class PlayDAO(models.Model, StatlerModel):
    """Represents a single performance in the database.

    The class/table contains static data regarding the performance. Data that will
    change over time will be store elsewhere."""

    # region Database Fields
    # Note: these lengths are arbitrary.
    url_title = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    # null refers to database structure. blank refers to Django validation.
    actors = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    image = models.FileField(upload_to="static", blank=True, null=True)
    show_times = models.CharField(max_length=256, blank=True)
    # endregion

    # region Method Overrides

    def __str__(self):
        """default string representation"""

        return self.title

    def getApiFields(self):
        """Gets fields for API serialization"""

        return {
            "url_title": self.url_title,
            "title": self.title,
            "director": self.director,
            "actors": self.actors,
            "show_times": self.show_times,
            "description": self.description,
            "image_url": (self.image.url if self.image else None),

            # TODO: self.rank = ??? (Look this up from DB)
            "rank": None,

            # TODO: Filter to top reviews only.
            "reviews": list(self.reviewdao_set.all())
        }
    # endregion
