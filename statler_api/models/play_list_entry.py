from django.db import models

from statler_api.models import PlayDAO, PlayListDAO, StatlerModel


class PlayListEntryDAO(models.Model, StatlerModel):
    """Glues together Plays and PlayLists in an optionally ordered fashion."""

    # region Database Fields
    play_list = models.ForeignKey(PlayListDAO)
    play = models.ForeignKey(PlayDAO)
    # Note that the order is optional.
    play_list_order = models.IntegerField(null=True, blank=True)
    # endregion

    # region Method Overrides
    def __str__(self):
        """default string representation"""

        return self.play.title + " in " + self.play_list.title

    def getApiFields(self):
        """Gets fields for API serialization"""

        return {
            "index": self.play_list_order,
            "play": self.play
        }
    # endregion
