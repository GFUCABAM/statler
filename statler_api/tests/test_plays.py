from unittest import expectedFailure
from django.test import TestCase
from statler_api.models import PlayDAO
from statler_api.api_models import Play


class PlayTestHelper:
    """Provides static data and functions to assist with end-to-end unit testing"""

    class Play1Vals:
        """Holds values with which to initialize play objects for testing."""
        url_title = "test-play-one"
        title = "Test Play One"
        director = "Test Director One"
        actors = "Test Actor One, Test Actor One Prime"
        description = "The first of the test plays."
        photo = None
        show_times = "The first time they test plays"

    class Play2Vals:
        """Holds values with which to initialize play objects for testing."""
        url_title = "test-play-two"
        title = "Test Play Two"
        director = "Test Director Two"
        actors = "Test Actor Two, Test Actor Two Prime"
        description = "The second of the test plays."
        photo = None
        show_times = "The second time they test plays"

    class PlayPrepersistedVals:
        """Holds values with which to pre-persist to the database a play for testing."""
        url_title = "test-play-prepersisted"
        title = "Test Play Prepersisted"
        director = "Test Director Prepersisted"
        actors = "Test Actor Prepersisted, Test Actor Prepersisted Prime"
        description = "A play which was saved to the database before testing commenced"
        photo = None
        show_times = "Before they even test plays"
        
    @staticmethod
    def assertDaoMatchesVals(dao, valClass, asserter):
        """ Assert that dao has values matching the valClass, using the TestCase instance asserter."""
        asserter.assertEquals(dao.url_title, valClass.url_title)
        asserter.assertEquals(dao.title, valClass.title)
        asserter.assertEquals(dao.director, valClass.director)
        asserter.assertEquals(dao.actors, valClass.actors)
        asserter.assertEquals(dao.description, valClass.description)
        asserter.assertEquals(dao.photo, valClass.photo)
        asserter.assertEquals(dao.show_times, valClass.show_times)
        
    @staticmethod
    def makeDao(valClass):
        """Initiates and returns a play data access object with the values contained in valClass"""

        dao = PlayDAO()
        
        dao.url_title = valClass.url_title
        dao.title = valClass.title
        dao.director = valClass.director
        dao.actors = valClass.actors
        dao.description = valClass.description
        dao.photo = valClass.photo
        dao.show_times = valClass.show_times

        return dao


class BasicPlaysTestCase(TestCase):
    """Testing the Plays table"""
    
    def setUp(self):
        """Prepare the class for the next test."""

        # Empty test database
        PlayDAO.objects.all().delete()

        # Initialize with the prepersisted DAO
        prepersistedDao = PlayTestHelper.makeDao(PlayTestHelper.PlayPrepersistedVals)
        prepersistedDao.save()

    def testCanGetPlay(self):
        """Test if we can save (in setUp) and get plays, with the expected values"""
        
        dao = PlayDAO.objects.get(url_title=PlayTestHelper.PlayPrepersistedVals.url_title)
        
        # Make sure we got something
        self.assertIsInstance(dao, PlayDAO)

        # Make sure the thing we got matches.
        PlayTestHelper.assertDaoMatchesVals(dao, PlayTestHelper.PlayPrepersistedVals, self)

    @expectedFailure
    def testCantGetNonexistentPlay(self):
        """Test that fetching a play which doesn't exist fails."""

        # This should throw an exception. Thus, the @expectedFailure annotation.
        dao = PlayDAO.objects.get(url_title="nonexistent-play")
        
    def testCanSavePlays(self):
        """Test if the play can be saved"""

        dao = PlayTestHelper.makeDao(PlayTestHelper.Play1Vals)

        # Make sure nothing's screwed up to start with
        PlayTestHelper.assertDaoMatchesVals(dao, PlayTestHelper.Play1Vals, self)

        # Save it!
        dao.save()

        # Assert that nothing changed
        PlayTestHelper.assertDaoMatchesVals(dao, PlayTestHelper.Play1Vals, self)

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

    def testPlayAPIFromDAO(self):
        """Tests conversion from a playDAO to an API Play"""

        # Populate DAO
        dao = PlayDAO()
        dao.url_title = PlayTestHelper.Play1Vals.url_title
        dao.title = PlayTestHelper.Play1Vals.title
        dao.director = PlayTestHelper.Play1Vals.director
        dao.actors = PlayTestHelper.Play1Vals.actors
        dao.description = PlayTestHelper.Play1Vals.description
        dao.photo = PlayTestHelper.Play1Vals.photo
        dao.show_times = PlayTestHelper.Play1Vals.show_times

        # Convert DAO to API object
        apiPlay = Play(dao)

        # Compare attributes
        # TODO: Once photos are implemented, test that too.
        self.assertEqual(apiPlay.url_title, PlayTestHelper.Play1Vals.url_title)
        self.assertEqual(apiPlay.title, PlayTestHelper.Play1Vals.title)
        self.assertEqual(apiPlay.director, PlayTestHelper.Play1Vals.director)
        self.assertEqual(apiPlay.actors, PlayTestHelper.Play1Vals.actors)
        self.assertEqual(apiPlay.description, PlayTestHelper.Play1Vals.description)
        # self.assertEqual(apiPlay.photo, PlayTestHelper.Play1Vals.photo)
        self.assertEqual(apiPlay.show_times, PlayTestHelper.Play1Vals.show_times)

    def testCanLoadPlayToAPI(self):
        """Tests saving a play, fetching that play, and creating an API object from the fetched play."""

        # Populate first dao
        dao1 = PlayTestHelper.makeDao(PlayTestHelper.Play1Vals)

        # Save dao1 to the database
        dao1.save()

        # Fetch the DAO
        dao2 = PlayDAO.objects.get(url_title=PlayTestHelper.Play1Vals.url_title)

        # Convert it to an API play
        apiPlay = Play(dao2)
        self.assertEqual(apiPlay.url_title, PlayTestHelper.Play1Vals.url_title)
        self.assertEqual(apiPlay.title, PlayTestHelper.Play1Vals.title)
        self.assertEqual(apiPlay.director, PlayTestHelper.Play1Vals.director)
        self.assertEqual(apiPlay.actors, PlayTestHelper.Play1Vals.actors)
        self.assertEqual(apiPlay.description, PlayTestHelper.Play1Vals.description)
        # self.assertEqual(apiPlay.photo, PlayTestHelper.Play1Vals.photo)
        self.assertEqual(apiPlay.show_times, PlayTestHelper.Play1Vals.show_times)



