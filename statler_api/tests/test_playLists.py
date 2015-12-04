from django.test import TestCase, TransactionTestCase
from statler_api.models import PlayList, PlayListEntry, Review
from statler_api.tests.test_plays import PlayTestHelper
from statler_api.tests.test_text_processing import SentimentTestHelper


class PlayListTestHelper:
    pass

class PlayListTestCase(TestCase):

    def testHappyCaseConversion(self):

        # Create (and save) the PlayList we're working with.
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

class TestPlayListRanking(TransactionTestCase):

    PLAY_LIST_URL_TITLE = "rtrtc-all-plays"

    def setUp(self):
        """ Create the list with which we'll test. """

        # region play list setup.
        # Save and store a reference to two new plays.
        self.positivePlay = PlayTestHelper.makePlay(PlayTestHelper.Play1Vals)
        self.positivePlay.save()

        self.neutralPlay = PlayTestHelper.makePlay(PlayTestHelper.PlayPrepersistedVals)
        self.neutralPlay.save()

        self.negativePlay = PlayTestHelper.makePlay(PlayTestHelper.Play2Vals)
        self.negativePlay.save()

        self.allPlayList = PlayList()
        self.allPlayList.title = "All ReviewToRankTestCase Plays"
        self.allPlayList.url_title = self.PLAY_LIST_URL_TITLE
        self.allPlayList.is_dynamically_ordered = True
        self.allPlayList.num_to_order_dynamically = 10  # Order them all.
        self.allPlayList.save()

        positivePlayEntry = PlayListEntry()
        positivePlayEntry.play = self.positivePlay
        positivePlayEntry.play_list = self.allPlayList
        positivePlayEntry.play_list_order = None
        positivePlayEntry.save()

        neutralPlayEntry = PlayListEntry()
        neutralPlayEntry.play = self.neutralPlay
        neutralPlayEntry.play_list = self.allPlayList
        neutralPlayEntry.play_list_order = 200
        neutralPlayEntry.save()

        negativePlayEntry = PlayListEntry()
        negativePlayEntry.play = self.negativePlay
        negativePlayEntry.play_list = self.allPlayList
        negativePlayEntry.play_list_order = 1
        negativePlayEntry.save()

        # We should now have a list of three plays.
        self.assertEqual(self.allPlayList.plays.count(), 3)
        # endregion

        # region review plays
        Review.createFromText(SentimentTestHelper.POSITIVE_REVIEW_TEXT, self.positivePlay.url_title)
        Review.createFromText(SentimentTestHelper.POSITIVE_REVIEW_TEXT, self.positivePlay.url_title)

        Review.createFromText(SentimentTestHelper.POSITIVE_REVIEW_TEXT, self.neutralPlay.url_title)
        Review.createFromText(SentimentTestHelper.NEGATIVE_REVIEW_TEXT, self.neutralPlay.url_title)

        Review.createFromText(SentimentTestHelper.NEGATIVE_REVIEW_TEXT, self.negativePlay.url_title)
        Review.createFromText(SentimentTestHelper.NEGATIVE_REVIEW_TEXT, self.negativePlay.url_title)

        # We should now have six reviews in the system.
        self.assertEqual(Review.objects.count(), 6)
        # endregion

        self.allPlayList.refresh_from_db()
        self.positivePlay.refresh_from_db()
        self.neutralPlay.refresh_from_db()
        self.negativePlay.refresh_from_db()

    def testDynamicallyOrdered(self):
        """ Test dynamically ordering a play list. """
        orderedPlays = self.allPlayList.getOrderedEntries()

        self.assertEqual(len(orderedPlays), 3)

        # make sure plays are sorted properly, and indices are properly set.
        self.assertEqual(orderedPlays[0].play.url_title, self.positivePlay.url_title)
        self.assertEqual(orderedPlays[0].play_list_order, 1)

        self.assertEqual(orderedPlays[1].play.url_title, self.neutralPlay.url_title)
        self.assertEqual(orderedPlays[1].play_list_order, 2)

        self.assertEqual(orderedPlays[2].play.url_title, self.negativePlay.url_title)
        self.assertEqual(orderedPlays[2].play_list_order, 3)

    def testStaticallyOrdered(self):
        """ Test statically ordering a play list. """

        self.allPlayList.is_dynamically_ordered = False
        self.allPlayList.save()

        orderedPlays = self.allPlayList.getOrderedEntries()

        self.assertEqual(len(orderedPlays), 3)

        # make sure plays are sorted properly, and indices are properly set.
        self.assertEqual(orderedPlays[0].play.url_title, self.negativePlay.url_title)
        self.assertEqual(orderedPlays[0].play_list_order, 1)

        self.assertEqual(orderedPlays[1].play.url_title, self.neutralPlay.url_title)
        self.assertEqual(orderedPlays[1].play_list_order, 2)

        self.assertEqual(orderedPlays[2].play.url_title, self.positivePlay.url_title)
        self.assertIsNone(orderedPlays[2].play_list_order)
