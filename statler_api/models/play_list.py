import random
from operator import attrgetter

from django.db import models


from statler_api.models import StatlerModel, Play


class PlayList(models.Model, StatlerModel):
    """A persisted list of plays."""

    # region Database Fields
    title = models.CharField(max_length=256)
    url_title = models.CharField(max_length=32)

    # Handle dynamically ordered lists. If order_dynamically, the plays' order will be determined by their ratings
    # at the server level. Only the top num_to_order_dynamically will be ordered. If !is_dynamically ordered,
    # num_to_order_dynamically has no effect.
    is_dynamically_ordered = models.BooleanField(default=False)
    num_to_order_dynamically = models.IntegerField(default=0)

    # See https://docs.djangoproject.com/en/dev/topics/db/models/#intermediary-manytomany
    # for documentation on this many-to-many pattern.
    plays = models.ManyToManyField(Play, through='PlayListEntry')
    # endregion

    # region Method Overrides
    def __str__(self):
        """default string representation"""

        return self.title

    def getApiFields(self):
        """Gets fields for API serialization

        Note that PlayList serializes as an array of nodes, not as a dictionary."""

        return self.getOrderedEntries()
    # endregion

    def getOrderedEntries(self):
        """ Orders the play's contained entries and adjusts the (in-memory) entries' index appropriately. """

        allPlays = list(self.playlistentry_set.all())
        orderedPlays = None
        unorderedPlays = None

        if self.is_dynamically_ordered:
            # Only plays which have been reviewed can be ranked dynamically.
            reviewedPlays = [p for p in allPlays if p.play.review_set.count() > 0]
            nonReviewedPlays = [p for p in allPlays if p.play.review_set.count() <= 0]

            reviewedPlays.sort(key=lambda p: p.play.rating, reverse=True)
            orderedPlays = reviewedPlays[:self.num_to_order_dynamically]
            unorderedPlays = reviewedPlays[self.num_to_order_dynamically:] + nonReviewedPlays

        else:
            orderedPlays = sorted([p for p in allPlays if p.play_list_order], key=lambda p: p.play_list_order)
            unorderedPlays = [p for p in allPlays if not p.play_list_order]

        # Properly index the ordered plays
        orderCounter = 1
        for p in orderedPlays:
            p.play_list_order = orderCounter
            orderCounter += 1

        # Shuffle and de-index the unordered plays
        for p in unorderedPlays:
            p.play_list_order = None
        random.shuffle(unorderedPlays)

        # Concatenate results.
        return orderedPlays + unorderedPlays

