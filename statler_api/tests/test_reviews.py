from django.test import TestCase
from statler_api.models import Review, Play
from django.utils import timezone

from statler_api.tests.test_plays import PlayTestHelper


class ReviewTestCase(TestCase):

    def testGetApiFields(self):
        review = Review()
        review.play = Play()
        review.timestamp = datetime.today()
        review.text = "foo"

        apiDict = review.getApiFields()

        self.assertEqual(apiDict, {"text": "foo", "timestamp": datetime.today().isoformat()})

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
