from django.db import models, transaction
from datetime import datetime

from statler_api.models import Play, StatlerModel
from statler_api import text_processing


class Review(models.Model, StatlerModel):
    """Represents a review of a play."""

    # region Database Fields
    play = models.ForeignKey(Play)
    text = models.TextField()
    rating = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)
    top_review_rank = models.IntegerField(null=True, blank=True, default=None)

    class Meta:
        # Disallow multiple "equally top" reviews on the same play.
        unique_together = ("play", "top_review_rank")

    # TODO Play rating ought to be dealt with at the database level. I'll leave it out for now.
    # play_rating = models.FloatField()
    # endregion

    # region Method Overrides
    def __str__(self):
        """default string representation: The first 32 characters of the review"""

        return self.text[:32] + ("..." if len(self.text) > 32 else "")

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
        # This shiould be handled at the DB level.
        # newReview.timestamp = datetime.now()
        newReview.rating = text_processing.rateReview(text)
        newReview.play = Play.objects.get(url_title=playUrlTitle)
        # newReview.playRatingSum = None
        # newReview.playReviewCount = None

        # Save it
        with transaction.atomic():

            # Lock the play
            newReview.play = Play.objects.select_for_update().get(url_title=playUrlTitle)

            # Ensure the new review is accounted for.
            newReview.save()

            playRatingQuery = newReview.play.review_set.aggregate(play_rating=models.Avg("rating"))
            newReview.play.rating = playRatingQuery["play_rating"]
            newReview.play.save()

            # lastReview = newReview.play.review_set.latest(field_name="timestamp")
            #
            # newReview.playRatingSum = lastReview.playRatingSum + newReview.rating
            # newReview.playReviewCount = lastReview.playReviewCount + 1


        # Give back the (now saved) review.
        return newReview
    # endregion
