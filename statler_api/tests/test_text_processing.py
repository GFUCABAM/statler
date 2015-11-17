from django.test import TestCase
from statler_api import text_processing


class SentimentTestCase(TestCase):
    """Tests our usage of the Sentiment API"""

    def testSimpleText(self):
        """Tests some simple text, checking that we get some result."""

        result = text_processing.rateReview("Simple test text.")
        self.assertIsNotNone(result)

    def testSimplePositive(self):
        """Tests simple, positive text, making sure we get a postive result."""

        result = text_processing.rateReview("This play was really good!")

        # Overtly positive text should return a result above 0.
        self.assertGreater(result, 0)

    def testSimpleNegative(self):
        """Tests some simple text, checkgin that we get some result."""

        result = text_processing.rateReview("This was the worst play I've ever seen.")

        # Overtly negative text should return a result below 0.
        self.assertLess(result, 0)
