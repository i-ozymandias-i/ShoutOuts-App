from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import ShoutOut

class ShoutOutManagerTests(TestCase):

    def setUp(self):
        """
        Create some users to test out out models
        :return:
        """

        User = get_user_model()
        self.user1 = User.objects.create_user('t1', 't1@example.com', 't1pass')
        self.user2 = User.objects.create_user('t2', 't2@example.com', 't2pass')

        self.approved = ShoutOut.objects.create(
            submitter= self.user1,
            body = 'Approved',
            approved = True,
            approved_by=self.user2,
        )

        self.unapproved = ShoutOut.objects.create(
            submitter=self.user1,
            body='Not Approved',
        )

    def test_public(self):
        self.assertTrue(self.approved in ShoutOut.objects.public())
        self.assertFalse(self.unapproved in ShoutOut.objects.public())

    def test_needs_approval(self):
        self.assertFalse(self.approved in ShoutOut.objects.needs_approval())
        self.assertTrue(self.unapproved in ShoutOut.objects.needs_approval())