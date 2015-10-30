from django.test import TestCase
from statler_api.models import PlayDAO


class BasicPlaysTestCase(TestCase):
    """Testing the Plays table"""

    def setUp(self):
        self.play = PlayDAO()

    def testCanSavePlays(self):
        """Test if the play can be saved"""
        self.play.director = "Director"
        self.play.url_title = "URL Title"
        self.play.title = "Title"

        self.play.save()

        self.assertEqual("Director", self.play.director)
        self.assertEqual("URL Title", self.play.url_title)
        self.assertEqual("Title", self.play.title)

    def testCanRefreshPlaysFromDatabase(self):
        """Test if the play can be updated and the updated version is refreshed from the database"""
        self.play.director = "Director"
        self.play.url_title = "URL Title"
        self.play.title = "Title"

        self.play.save()

        # This updates the title of all plays in the database. This may be a bad idea.
        PlayDAO.objects.update(title="New Title")

        self.play.refresh_from_db()
        self.assertEqual("New Title", self.play.title)