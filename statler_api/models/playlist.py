from django.db import models


class PlayListDAO(models.Model):
    """A persisted list of plays."""

    title = models.CharField(max_length=256)
    url_title = models.CharField(max_length=32)

    def __str__(self):
        """default string representation"""

        return self.title
