<<<<<<< HEAD
from django.test import TestCase
from statler_api.models import Review, Play
from django.utils import timezone

from statler_api.tests.test_plays import PlayTestHelper
=======
from django.test import TestCase, TransactionTestCase
from unittest import skip

from statler_api import text_processing
from statler_api.models import Review, Play
from datetime import datetime

from statler_api.tests.test_plays import PlayTestHelper
from statler_api.tests.test_text_processing import SentimentTestHelper
>>>>>>> refs/remotes/origin/dev


class ReviewTestCase(TestCase):

    def testGetApiFields(self):
        review = Review()
        review.play = Play()
        review.timestamp = datetime.today()
        review.text = "foo"

        apiDict = review.getApiFields()

        self.assertEqual(apiDict, {"text": "foo", "timestamp": datetime.today().isoformat()})

<<<<<<< HEAD
=======
    @skip  # Skipping until #104 is resolved.
>>>>>>> refs/remotes/origin/dev
    def testCreateFromText(self):

        startTimeStamp = datetime.now()

        # Set up a play to reference.
        play = PlayTestHelper.makePlay(PlayTestHelper.Play1Vals)
        play.save()

        theReview = Review.createFromText("The play was foo.", play.url_title)

        self.assertEqual(theReview.text, "The play was foo.")
        self.assertIsNotNone(theReview.rating)
        self.assertEqual(theReview.play, play)

        # Check the timestamp against some bounds.
        endTimeStamp = datetime.now()
        self.assertGreaterEqual(theReview.timestamp, startTimeStamp)
        self.assertLessEqual(theReview.timestamp, endTimeStamp)
<<<<<<< HEAD
=======

class ReviewToRankTestCase(TransactionTestCase):
    """ Tests rating and ranking plays through multiple reviews.

    Extends TransactionTestCase, because there's transaction-related database things happening."""

    play_url_title = PlayTestHelper.PlayPrepersistedVals.url_title
    positive_rating = text_processing.rateReview(SentimentTestHelper.POSITIVE_REVIEW_TEXT)
    negative_rating = text_processing.rateReview(SentimentTestHelper.NEGATIVE_REVIEW_TEXT)

    def setUp(self):
        """ Persist a play we can use for testing. """
        PlayTestHelper.makePlay(PlayTestHelper.PlayPrepersistedVals).save()

    def getPlay(self):
        """ Fetch the play this class uses for testing. """
        return Play.objects.get(url_title=self.play_url_title)

    def testInitialPlayRating(self):
        """ Make sure the play starts out with a rating of zero. """
        self.assertEqual(self.getPlay().rating, 0)

    def testSinglePositiveReviewRating(self):
        """ Make sure rating one play positively works as expected. """

        Review.createFromText(SentimentTestHelper.POSITIVE_REVIEW_TEXT, self.play_url_title)
        self.assertEqual(self.getPlay().rating, self.positive_rating)

    def testSingleNegativeReviewRating(self):
        """ Make sure rating one play negatively works as expected. """

        Review.createFromText(SentimentTestHelper.POSITIVE_REVIEW_TEXT, self.play_url_title)
        self.assertEqual(self.getPlay().rating, self.positive_rating)

    def testAveragingTwoReviewRatings(self):
        """ Make sure rating a play twice, differently, correctly averages those ratings."""

        Review.createFromText(SentimentTestHelper.NEGATIVE_REVIEW_TEXT, self.play_url_title)
        Review.createFromText(SentimentTestHelper.POSITIVE_REVIEW_TEXT, self.play_url_title)

        expectedRating = (self.positive_rating + self.negative_rating) / 2

        # Allow rounding errors more than 7 decimal places out.
        self.assertAlmostEqual(self.getPlay().rating, expectedRating, places=7)
>>>>>>> refs/remotes/origin/dev
