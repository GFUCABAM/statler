from django.db import models

from statler_api.models import StatlerModel, Play


class PlayList(models.Model, StatlerModel):
    """A persisted list of plays."""

    # region Database Fields
    title = models.CharField(max_length=256)
    url_title = models.CharField(max_length=32)

    # See https://docs.djangoproject.com/en/dev/topics/db/models/#intermediary-manytomany
    # for documentation on this many-to-many pattern.
    plays = models.ManyToManyField(Play, through='PlayListEntry')
    # endregion

    # region Method Overrides
    def __str__(self):
        """default string representation"""

        return self.title

    def getApiFields(self):
        """Gets fields for API serialization

        Note that PlayList serializes as an array of nodes, not as a dictionary."""

        return list(self.playlistentry_set.all())
    # endregion
