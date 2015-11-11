from django.db import models

from statler_api.models import PlayDAO, StatlerModel


class ReviewDAO(models.Model, StatlerModel):
    """Represents a review of a play."""

    # region Database Fields
    play = models.ForeignKey(PlayDAO)
    text = models.TextField()
    rating = models.FloatField()
    timestamp = models.DateTimeField()

    # TODO Play rating ought to be dealt with at the database level. I'll leave it out for now.
    # play_rating = models.FloatField()
    # endregion

    # region Method Overrides
    def __str__(self):
        """default string representation: The first 16 characters of the review"""

        return self.text[:16]

    def getApiFields(self):
        """Gets fields for API serialization"""

        return {
            "text": self.text,
            "timestamp": self.timestamp.isoformat()
        }
    # endregion
