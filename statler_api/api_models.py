"""Classes which represent objects above the database level."""
from datetime import datetime
from .models import PlayDAO
from .models import PlayListDAO
from .models import PlayListEntryDAO
from .models import ReviewDAO
from statler_api import text_processing

class NewReview:
    """Represents a new review, prior to being saved in the database."""

    # TODO: Figure out automatic serialization from the JSON request.

    def __init__(self, playUrlTitle, text):
        """ Construct a new review from posted text, calculating required values """

        self.text = text
        self.playUrlTitle = playUrlTitle

        # TODO: Push timestamping into the database.
        # timestamp the new review right now.
        self.timestamp = datetime.now()

        # Fetch the rating externally
        self.rating = text_processing.rateReview(text)

    def toDao(self):
        """ Readies the review for database insertion.

        :return: A ReviewDAO, created from the new review.
        """
        dao = ReviewDAO()

        dao.text = self.text
        dao.timestamp = self.timestamp
        dao.rating = self.rating

        # Fetch the play to reference
        dao.play = PlayDAO.objects.get(url_title=self.playUrlTitle)

        return dao
