"""Classes which represent objects above the database level."""

from .models import *


class Play:
    """Represents a play object."""

    def __init__(self, dao=None, urlTitle=None, title=None, director=None, actors=None, showTimes=None, description=None, imageUrl=None, rank=None):
        """Constructs a new Play object

        First, if dao is defined, fields from the DAO are bound into the new object.
        Second, other named parameters are bound, overriding the DAO if relevant.
        """

        # dao will be "truthy" if it's non-null (https://docs.python.org/3.4/reference/datamodel.html#object.__bool__)
        if dao:
            # Confirm we have the right sort of DAO
            assert isinstance(dao, PlayDAO)

            # Bind DAO fields to the new instance.
            self.urlTitle = dao.url_title
            self.title = dao.title
            self.director = dao.director
            self.actors = dao.actors
            self.showTimes = dao.show_times
            self.description = dao.description
            # TODO: Resolve naming discrepancy
            self.imageUrl = dao.photo

            # TODO: self.rank = ??? (Look this up from DB)
            self.rank = None

            # TODO: Deal with binding reviews?

        # Bind any non-null named parameters, overriding the DAO if neccesary
        if urlTitle:
            self.urlTitle = urlTitle
        if title:
            self.title = title
        if director:
            self.director = director
        if actors:
            self.actors = actors
        if showTimes:
            self.showTimes = showTimes
        if description:
            self.description = description
        if imageUrl:
            self.imageUrl = imageUrl
        if rank:
            self.rank = rank


class Review:
    """Represents a review object."""

    def __init__(self, dao=None, text=None, date=None):
        """Constructs a new Review object

        First, if dao is defined, fields from the DAO are bound into the new object.
        Second, other named parameters are bound, overriding the DAO if relevant.

        Note that this object doesn't currently contain a rating, due to serialization concerns.
        This will need to be addressed when we write the POST endpoint.
        """

        # dao will be "truthy" if it's non-null (https://docs.python.org/3.4/reference/datamodel.html#object.__bool__)
        if dao:
            # Confirm we have the right sort of DAO
            assert isinstance(dao, ReviewDAO)

            # Bind DAO fields to the new instance.
            self.text = dao.text
            # TODO: Resolve naming discrepancy
            self.date = dao.timestamp


        # Bind any non-null named parameters, overriding the DAO if neccesary
        if text:
            self.text = text
        if date:
            self.date = date


class PlayListEntry:
    """Represents a node in a PlayList. Essentially meaningless outside of PlayList object"""

    def __init__(self, dao=None, index=None, play=None):
        """Constructs a new PlayListEntry object

        First, if dao is defined, fields from the DAO are bound into the new object.
        Second, other named parameters are bound, overriding the DAO if relevant.
        """

        if dao:
            # Confirm we have the right sort of DAO
            assert isinstance(dao, PlayListEntryDAO)

            # Bind DAO fields to the new instance.
            self.index = dao.play_list_order

            # Convert PlayDAO to non-DAO
            self.play = Play(dao.play)

        # Bind any non-null named parameters, overriding the DAO if neccesary
        if index:
            self.index = index
        if play:
            self.play = play


class PlayList:
    """Represents a play list object."""

    def __init__(self, dao=None, urlTitle=None, entries=None):
        """Constructs a new PlayLisrt object

        First, if dao is defined, fields from the DAO are bound into the new object.
        Second, other named parameters are bound, overriding the DAO if relevant.
        """

        # dao will be "truthy" if it's non-null (https://docs.python.org/3.4/reference/datamodel.html#object.__bool__)
        if dao:
            # Confirm we have the right sort of DAO
            assert isinstance(dao, PlayListDAO)

            # Bind DAO fields to the new instance.
            self.urlTitle = dao.url_title

            # Convert contained DAOs to non-DAOs through a list comprehension
            # (https://docs.python.org/3.4/tutorial/datastructures.html#list-comprehensions)
            self.entries = [PlayListEntry(entryDao) for entryDao in dao.playlistentrydao_set]

        # Bind any non-null named parameters, overriding the DAO if neccesary
        if urlTitle:
            self.urlTitle = urlTitle

        if entries:
            self.entries = entries
