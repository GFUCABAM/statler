from django.test import TestCase
from statler_api.models import PlayDAO
from statler_api.api_models import Play


class BasicPlaysTestCase(TestCase):
    """Testing the Plays table"""

    def testCanSavePlays(self):
        """Test if the play can be saved"""

        play = PlayDAO()

        play.director = "Director"
        play.url_title = "URL Title"
        play.title = "Title"

        play.save()

        self.assertEqual("Director", play.director)
        self.assertEqual("URL Title", play.url_title)
        self.assertEqual("Title", play.title)

    def testCanRefreshPlaysFromDatabase(self):
        """Test if the play can be updated and the updated version is refreshed from the database"""

        play = PlayDAO()

        play.director = "Director"
        play.url_title = "URL Title"
        play.title = "Title"

        play.save()

        # This updates the title of all plays in the database. This may be a bad idea, but for now it works.
        PlayDAO.objects.update(title="New Title")

        play.refresh_from_db()
        self.assertEqual("New Title", play.title)


class APIPlaysTestCase(TestCase):
    """ Testing the plays at the API level, as well as conversion from the DAOs. """

    class Play1Vals(object):
        """Holds values with which to initialize play objects for testing."""
        urlTitle = "test-play-one"
        title = "Test Play One"
        director = "Test Director One"
        actors = "Test Actor One, Test Actor One'"
        description = "The first of the test plays."
        photo = None
        show_times = "The first time they test plays"

    def testPlayAPIFromDAO(self):
        """Tests conversion from a playDAO to an API Play"""

        # Populate DAO
        dao = PlayDAO()
        dao.url_title = APIPlaysTestCase.Play1Vals.urlTitle
        dao.title = APIPlaysTestCase.Play1Vals.title
        dao.director = APIPlaysTestCase.Play1Vals.director
        dao.actors = APIPlaysTestCase.Play1Vals.actors
        dao.description = APIPlaysTestCase.Play1Vals.description
        dao.photo = APIPlaysTestCase.Play1Vals.photo
        dao.show_times = APIPlaysTestCase.Play1Vals.show_times

        # Convert DAO to API object
        apiPlay = Play(dao)

        # Compare attributes
        # TODO: Once photos are implemented, test that too.
        self.assertEqual(apiPlay.url_title, APIPlaysTestCase.Play1Vals.urlTitle)
        self.assertEqual(apiPlay.title, APIPlaysTestCase.Play1Vals.title)
        self.assertEqual(apiPlay.director, APIPlaysTestCase.Play1Vals.director)
        self.assertEqual(apiPlay.actors, APIPlaysTestCase.Play1Vals.actors)
        self.assertEqual(apiPlay.description, APIPlaysTestCase.Play1Vals.description)
        # self.assertEqual(apiPlay.photo, APIPlaysTestCase.Play1Vals.photo)
        self.assertEqual(apiPlay.show_times, APIPlaysTestCase.Play1Vals.show_times)

    def testCanLoadPlayToAPI(self):
        """Tests saving a play, fetching that play, and creating an API object from the fetched play."""

        # Populate first dao
        dao1 = PlayDAO()
        dao1.url_title = APIPlaysTestCase.Play1Vals.urlTitle
        dao1.title = APIPlaysTestCase.Play1Vals.title
        dao1.director = APIPlaysTestCase.Play1Vals.director
        dao1.actors = APIPlaysTestCase.Play1Vals.actors
        dao1.description = APIPlaysTestCase.Play1Vals.description
        dao1.photo = APIPlaysTestCase.Play1Vals.photo
        dao1.show_times = APIPlaysTestCase.Play1Vals.show_times

        # Save dao1 to the database
        dao1.save()

        # Fetch the DAO
        dao2 = PlayDAO.objects.get(url_title=APIPlaysTestCase.Play1Vals.urlTitle)

        # Convert it to an API play
        apiPlay = Play(dao2)
        self.assertEqual(apiPlay.url_title, APIPlaysTestCase.Play1Vals.urlTitle)
        self.assertEqual(apiPlay.title, APIPlaysTestCase.Play1Vals.title)
        self.assertEqual(apiPlay.director, APIPlaysTestCase.Play1Vals.director)
        self.assertEqual(apiPlay.actors, APIPlaysTestCase.Play1Vals.actors)
        self.assertEqual(apiPlay.description, APIPlaysTestCase.Play1Vals.description)
        # self.assertEqual(apiPlay.photo, APIPlaysTestCase.Play1Vals.photo)
        self.assertEqual(apiPlay.show_times, APIPlaysTestCase.Play1Vals.show_times)



