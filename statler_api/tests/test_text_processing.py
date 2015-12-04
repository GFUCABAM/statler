from django.test import TestCase
from statler_api import text_processing

class SentimentTestHelper:

    POSITIVE_REVIEW_TEXT = "This play was really good!"
    NEGATIVE_REVIEW_TEXT = "This was the worst play I've ever seen."

class SentimentTestCase(TestCase):
    """Tests our usage of the Sentiment API"""

    def testSimpleText(self):
        """Tests some simple text, checking that we get some result."""

        result = text_processing.rateReview("Simple test text.")
        self.assertIsNotNone(result)

    def testSimplePositive(self):
        """Tests simple, positive text, making sure we get a positive result."""

        result = text_processing.rateReview(SentimentTestHelper.POSITIVE_REVIEW_TEXT)

        # Overtly positive text should return a result above 0.
        self.assertGreater(result, 0)

    def testSimpleNegative(self):
        """Tests simple, negative text, making sure we get a negative result."""

        result = text_processing.rateReview(SentimentTestHelper.NEGATIVE_REVIEW_TEXT)

        # Overtly negative text should return a result below 0.
        self.assertLess(result, 0)
