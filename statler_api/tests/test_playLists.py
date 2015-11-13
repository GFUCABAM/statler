from django.test import TestCase
from statler_api.models import PlayList, PlayListEntry
from statler_api.tests.test_plays import PlayTestHelper


class PlayListTestHelper:
    pass

class PlayListTestCase(TestCase):

    def testHappyCaseConversion(self):

        # Create (and save) the PlayListDao we're working with.
        theList = PlayList()
        theList.title = "Test Play List"
        theList.url_title = "test-play-list"
        theList.save()

        # Create (and save) a pair of plays to populate the Play
        play1 = PlayTestHelper.makePlay(PlayTestHelper.Play1Vals);
        play2 = PlayTestHelper.makePlay(PlayTestHelper.Play2Vals);
        play1.save()
        play2.save()

        # Create* a pair of entries to bind the plays to the list
        playListEntry1 = PlayListEntry()
        playListEntry1.play = play1
        playListEntry1.play_list = theList
        playListEntry1.play_list_order = 1

        playListEntry2 = PlayListEntry()
        playListEntry2.play = play2
        playListEntry2.play_list = theList
        playListEntry2.play_list_order = 2

        # *(and save)
        playListEntry1.save()
        playListEntry2.save()

        # Update the list, so that it picks up changes
        theList.refresh_from_db()

        # Convert it to API Fields
        apiList = theList.getApiFields()

        # Check things.
        self.assertEquals(len(apiList), 2)
        # TODO: Check more things.






