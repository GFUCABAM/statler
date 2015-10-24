"""Classes which represent objects above the database level."""

from .models import *


class Play:
    """Represents a play object."""

    def __init__(self, dao=None, urlTitle=None, director=None, actors=None, showTimes=None, description=None, imageUrl=None, rank=None):
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
            self.director = dao.director
            self.actors = dao.actors
            self.showTimes = dao.show_times
            self.description = dao.description
            # TODO: Resolve naming discrepancy
            self.imageUrl = dao.photo

            # TODO: self.rank = ??? (Look this up from DB)

        # Bind any non-null named parameters, overriding the DAO if neccesary
        if urlTitle:
            self.urlTitle = urlTitle
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
    pass


class PlayList:
    pass
