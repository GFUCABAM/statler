from django.db import models

from statler_api.models import Play, PlayList, StatlerModel


class PlayListEntry(models.Model, StatlerModel):
    """Glues together Plays and PlayLists in an optionally ordered fashion."""

    # region Database Fields
    play_list = models.ForeignKey(PlayList, on_delete=models.CASCADE)
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
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

            # include only the fields required when in a list on the play.
            "play": self.play.getPlayListApiFields()
        }
    # endregion
