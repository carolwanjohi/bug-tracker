import unittest
# Import class to be tested
from app.models import BugCard

class BugCardTest(unittest.TestCase):
    '''
    Test class to test behaviours of the BugCard class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_bug_card = BugCard(1927,'Bug Card Name','https//card-url.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_bug_card,BugCard))

    def test_init(self):
        self.assertEqual(self.new_bug_card.id, 1927)
        self.assertEqual(self.new_bug_card.name,'Bug Card Name')
        self.assertEqual(self.new_bug_card.url,'https//card-url.com')