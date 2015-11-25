from unittest import expectedFailure
from django.test import TestCase
<<<<<<< HEAD
from statler_api.models import PlayDAO
from statler_api.api_models import Play
from django.utils import timezone
=======
from statler_api.models import Play
>>>>>>> refs/remotes/origin/dev


class PlayTestHelper:
    """Provides static data and functions to assist with end-to-end unit testing"""

    class Play1Vals:
        """Holds values with which to initialize play objects for testing."""
        url_title = "test-play-one"
        title = "Test Play One"
        director = "Test Director One"
        actors = "Test Actor One, Test Actor One Prime"
        description = "The first of the test plays."
        image = None
        show_times = "The first time they test plays"

    class Play2Vals:
        """Holds values with which to initialize play objects for testing."""
        url_title = "test-play-two"
        title = "Test Play Two"
        director = "Test Director Two"
        actors = "Test Actor Two, Test Actor Two Prime"
        description = "The second of the test plays."
        image = None
        show_times = "The second time they test plays"

    class PlayPrepersistedVals:
        """Holds values with which to pre-persist to the database a play for testing."""
        url_title = "test-play-prepersisted"
        title = "Test Play Prepersisted"
        director = "Test Director Prepersisted"
        actors = "Test Actor Prepersisted, Test Actor Prepersisted Prime"
        description = "A play which was saved to the database before testing commenced"
        image = None
        show_times = "Before they even test plays"
        
    @staticmethod
    def assertPlayMatchesVals(play, valClass, asserter):
        """ Assert that dao has values matching the valClass, using the TestCase instance asserter."""
        asserter.assertEquals(play.url_title, valClass.url_title)
        asserter.assertEquals(play.title, valClass.title)
        asserter.assertEquals(play.director, valClass.director)
        asserter.assertEquals(play.actors, valClass.actors)
        asserter.assertEquals(play.description, valClass.description)
        # asserter.assertEquals(dao.image, valClass.image)
        asserter.assertEquals(play.show_times, valClass.show_times)
        
    @staticmethod
    def makePlay(valClass):
        """Initiates and returns a play data access object with the values contained in valClass"""

        dao = Play()
        
        dao.url_title = valClass.url_title
        dao.title = valClass.title
        dao.director = valClass.director
        dao.actors = valClass.actors
        dao.description = valClass.description
        dao.image = valClass.image
        dao.show_times = valClass.show_times

        return dao


class PlayDAOTestCase(TestCase):
    """Testing the Plays table"""
    
    def setUp(self):
        """Prepare the class for the next test."""

        # Empty test database
        Play.objects.all().delete()

        # Initialize with the prepersisted DAO
        prepersistedDao = PlayTestHelper.makePlay(PlayTestHelper.PlayPrepersistedVals)
        prepersistedDao.save()

    def testCanGetPlay(self):
        """Test if we can save (in setUp) and get plays, with the expected values"""
        
        dao = Play.objects.get(url_title=PlayTestHelper.PlayPrepersistedVals.url_title)
        
        # Make sure we got something
        self.assertIsInstance(dao, Play)

        # Make sure the thing we got matches.
        PlayTestHelper.assertPlayMatchesVals(dao, PlayTestHelper.PlayPrepersistedVals, self)

    @expectedFailure
    def testCantGetNonexistentPlay(self):
        """Test that fetching a play which doesn't exist fails."""

        # This should throw an exception. Thus, the @expectedFailure annotation.
        dao = Play.objects.get(url_title="nonexistent-play")
        
    def testCanSavePlays(self):
        """Test if the play can be saved"""

        dao = PlayTestHelper.makePlay(PlayTestHelper.Play1Vals)

        # Make sure nothing's screwed up to start with
        PlayTestHelper.assertPlayMatchesVals(dao, PlayTestHelper.Play1Vals, self)

        # Save it!
        dao.save()

        # Assert that nothing changed
        PlayTestHelper.assertPlayMatchesVals(dao, PlayTestHelper.Play1Vals, self)

    def testCanRefreshPlaysFromDatabase(self):
        """Test if the play can be updated and the updated version is refreshed from the database"""

        play = Play()

        play.director = "Director"
        play.url_title = "URL Title"
        play.title = "Title"

        play.save()

        # This updates the title of all plays in the database. This may be a bad idea, but for now it works.
        Play.objects.update(title="New Title")

        play.refresh_from_db()
        self.assertEqual("New Title", play.title)


