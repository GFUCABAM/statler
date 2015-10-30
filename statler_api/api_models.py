"""Classes which represent objects above the database level."""

import time
from .models import *


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
        # TODO: Resolve naming discrepancy
        self.image_url = dao.photo

        # TODO: self.rank = ??? (Look this up from DB)
        self.rank = None

        # Map the play's review DAOs to review API objects
        # TODO: Filter to top reviews only.
        self.reviews = [Review(r) for r in dao.reviewdao_set.all()]


class Review:
    """Represents a review object, """

    def __init__(self, dao=None, text=None, date=None):
        """Constructs a previously-posted review object from a DAO"""

        # Confirm we have the right sort of DAO
        assert isinstance(dao, ReviewDAO)

        # Bind DAO fields to the new instance.
        self.text = dao.text
        # TODO: Resolve naming discrepancy
        self.date = dao.timestamp

# TODO: Work in progress.
# class NewReview:
#     """Represents a new review, prior to being saved in the database."""
#
#     # TODO: Figure out automatic serialization from the JSON request.
#
#     def __init__(self, playUrlTitle, text):
#         """Construct a new review from posted text"""
#
#         self.text = text
#         self.playUrlTitle = playUrlTitle
#
#         # timestamp the new review right now.
#         self.timestamp = time.time()
#
#     def toDao(self):
#         dao = ReviewDAO()
#
#         dao.text = self.text
#         dao.timestamp = self.timestamp


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
