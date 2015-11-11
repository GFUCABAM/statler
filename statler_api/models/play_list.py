from django.db import models

from statler_api.models import StatlerModel


class PlayListDAO(models.Model, StatlerModel):
    """A persisted list of plays."""

    # region Database Fields
    title = models.CharField(max_length=256)
    url_title = models.CharField(max_length=32)
    # endregion

    # region Method Overrides
    def __str__(self):
        """default string representation"""

        return self.title

    def getApiFields(self):
        """Gets fields for API serialization"""

        return {
            "url_title": self.url_title,
            "entries": list(self.playlistentrydao_set.all())
        }
    # endregion
