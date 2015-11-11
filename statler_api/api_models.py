"""Classes which represent objects above the database level."""
from datetime import datetime
from .models import PlayDAO
from .models import PlayListDAO
from .models import PlayListEntryDAO
from .models import ReviewDAO
from statler_api import text_processing


class Play:
    """Represents a play object."""

    def __init__(self, dao):
        """Constructs a new Play object from a DAO"""

        # Confirm we have the right sort of DAO
        assert isinstance(dao, PlayDAO)

        # Bind DAO fields to the new instance.
        self.url_title = dao.url_title
        self.title = dao.title
        self.director = dao.director
        self.actors = dao.actors
        self.show_times = dao.show_times
        self.description = dao.description
        self.image_url = (dao.image.url if dao.image else None)

        # TODO: self.rank = ??? (Look this up from DB)
        self.rank = None

        # Map the play's review DAOs to review API objects
        # TODO: Filter to top reviews only.
        self.reviews = TopReviews(dao.topreviewdao_set)


class Review:
    """Represents a review object, """

    def __init__(self, dao, rank):
        """Constructs a previously-posted review object from a DAO"""

        # Confirm we have the right sort of DAO
        assert isinstance(dao, ReviewDAO)

        # Bind DAO fields to the new instance.
        self.text = dao.text
        self.timestamp = dao.timestamp


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


class PlayListEntry:
    """Represents a node in a PlayList. Essentially meaningless outside of PlayList object"""

    def __init__(self, dao):
        """Constructs a new PlayListEntry object from a DAO."""

        # Confirm we have the right sort of DAO
        assert isinstance(dao, PlayListEntryDAO)

        # Bind DAO fields to the new instance.
        self.index = dao.play_list_order

        # Convert PlayDAO to non-DAO
        self.play = Play(dao.play)


class PlayList:
    """Represents a play list object."""

    def __init__(self, dao):
        """Constructs a new PlayList object from a DAO"""

        # Confirm we have the right sort of DAO
        assert isinstance(dao, PlayListDAO)

        # Bind DAO fields to the new instance.
        self.url_title = dao.url_title

        # Map contained DAOs to non-DAOs
        self.entries = [PlayListEntry(p) for p in dao.playlistentrydao_set.all()]

class TopReviews:
    """Collects a play's top reviews."""

    def __init__(self, topReviewDAOSet):
        """Create an object containing the top reviews to display with a play."""

        allTopReviews = sorted(list(topReviewDAOSet.all()),
                               key=lambda r: r.review_order)

        if len(allTopReviews) >= 1:
            self.topReview1 = Review(allTopReviews[0])
        if len(allTopReviews) >= 2:
            self.topReview2 = Review(allTopReviews[1])
        if len(allTopReviews) >= 3:
            self.topReview3 = Review(allTopReviews[2])