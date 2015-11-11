from django.test import TestCase
from statler_api.models import PlayList, PlayListEntry
from statler_api.tests.test_plays import PlayTestHelper


class PlayListTestHelper:
    pass

# class PlayListTestCase(TestCase):
#
#     def testHappyCaseConversion(self):
#
#         # Create (and save) the PlayListDao we're working with.
#         dao = PlayListDAO()
#         dao.title = "Test Play List"
#         dao.url_title = "test-play-list"
#         dao.save()
#
#         # Create (and save) a pair of plays to populate the DAO
#         playDao1 = PlayTestHelper.makePlay(PlayTestHelper.Play1Vals);
#         playDao2 = PlayTestHelper.makePlay(PlayTestHelper.Play2Vals);
#         playDao1.save()
#         playDao2.save()
#
#         # Create* a pair of entries to bind the plays to the list
#         playListEntryDao1 = PlayListEntryDAO()
#         playListEntryDao1.play = playDao1
#         playListEntryDao1.play_list = dao
#         playListEntryDao1.play_list_order = 1
#
#         playListEntryDao2 = PlayListEntryDAO()
#         playListEntryDao2.play = playDao2
#         playListEntryDao2.play_list = dao
#         playListEntryDao2.play_list_order = 2
#
#         # *(and save)
#         playListEntryDao1.save()
#         playListEntryDao2.save()
#
#         # Update the list, so that it picks up changes
#         dao.refresh_from_db()
#
#         # Convert it to an API object
#         apiList = PlayList(dao)
#
#         # Check things.
#         self.assertEquals(apiList.url_title, dao.url_title)
#         self.assertEquals(len(apiList.entries), 2)
#         # TODO: Check more things.






