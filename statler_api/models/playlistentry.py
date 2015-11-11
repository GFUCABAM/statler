from django.db import models

from statler_api.models import PlayDAO, PlayListDAO


class PlayListEntryDAO(models.Model):
    """Glues together Plays and PlayLists in an optionally ordered fashion."""

    play_list = models.ForeignKey(PlayListDAO)
    play = models.ForeignKey(PlayDAO)
    # Note that the order is optional.
    play_list_order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """default string representation"""

        return self.play.title + " in " + self.play_list.title
