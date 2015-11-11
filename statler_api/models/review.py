from django.db import models
from datetime import datetime

from statler_api.models import Play, StatlerModel
from statler_api import text_processing


class Review(models.Model, StatlerModel):
    """Represents a review of a play."""

    # region Database Fields
    play = models.ForeignKey(Play)
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

    # region Static Methods
    @staticmethod
    def createFromText(text, playUrlTitle):
        """ Creates and saves a review from the passed text and playUrlTitle, setting other fields appropriately."""


        # Create the new review
        newReview = Review()
        newReview.text = text
        newReview.timestamp = datetime.now()
        newReview.rating = text_processing.rateReview(text)
        newReview.play = Play.objects.get(url_title=playUrlTitle)

        # Save it
        newReview.save()

        # Give back the (now saved) review.
        return newReview
    # endregion
