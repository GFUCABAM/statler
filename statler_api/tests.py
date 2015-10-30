from django.test import TestCase
from statler_api.models import Play

# Testing the Plays table
class BasicPlaysTestCase(TestCase):

    def setUp(self):
        self.play = Play()

    # Test if the play can be saved
    def testCanSavePlays(self):
        self.play.director = "Director"
        self.play.url_title = "URL Title"
        self.play.title = "Title"

        self.play.save()

        self.assertEqual("Director", self.play.director)
        self.assertEqual("URL Title", self.play.url_title)
        self.assertEqual("Title", self.play.title)

    # Test if the play can be updated and the updated version is refreshed from the database
    def testCanRefreshPlaysFromDatabase(self):
        self.play.director = "Director"
        self.play.url_title = "URL Title"
        self.play.title = "Title"

        self.play.save()

        self.play.update(title = "New Title")

        self.play.refresh_from_db()
        self.assertEqual("New Title", self.play.title)

    def tearDown(self):
        self.play.dispose()