from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import ShoutOut

class ShoutOutModelTests(TestCase):

    def setUp(self):
        """
        Create some users to test out our models
        :return:
        """

        User = get_user_model()
        self.user1 = User.objects.create_user('t1', 't1@example.com', 't1pass')
        self.user2 = User.objects.create_user('t2', 't2@example.com', 't2pass')
        self.user3 = User.objects.create_user('t3', 't3@example.com', 't3pass')

    def test_no_mention_model(self):
        s = ShoutOut.objects.create_shoutout(
            submitter=self.user1,
            body='this is a test',
        )
        self.assertFalse(s.approved)
        self.assertEqual(s.mention_count,0)

    def test_single_mention(self):
        s=ShoutOut.objects.create_shoutout(
            submitter=self.user1,
            body='This is a test with @t1 mention',
        )

        self.assertFalse(s.approved)
        self.assertEqual(s.mention_count, 1)

    def test_double_mention(self):
        s=ShoutOut.objects.create_shoutout(
            submitter=self.user1,
            body='This is a test with @t1 mention and a @t2',
        )

        self.assertFalse(s.approved)
        self.assertEqual(s.mention_count, 2)