from django.db import models

from statler_api.models import PlayDAO


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
