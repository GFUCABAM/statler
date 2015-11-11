from django.test import TestCase
from statler_api.models import ReviewDAO, PlayDAO
from datetime import datetime

class ReviewTestCase(TestCase):

    def testGetApiFields(self):
        review = ReviewDAO()
        review.play = PlayDAO()
        review.timestamp = datetime.today()
        review.text = "foo"

        apiDict = review.getApiFields()

        self.assertEqual(apiDict, {"text": "foo", "timestamp": datetime.today()})
