import re
from django.contrib.auth import get_user_model
from django.db.models.loading import get_model
from django.db.models import Manager
from django.db.models.query import QuerySet


class ShoutOutQuerySet(QuerySet):
    """ Custom QuerySet for ShoutOuts
    """

    def public(self):
        return self.filter(approved=True)

    def needs_approval(self):
        return self.filter(approved=False)

class ShoutOutManager(Manager):

    def get_queryset(self):
        """
        Make our default manager use our new QuerySet
        """
        return ShoutOutQuerySet(self.model, using=self._db)

    def create_shoutout(self, submitter, body):
        """
        Find all users mentions in ShoutOut body and create Mention objects.
        """
        ShoutOut = get_model('shoutouts', 'ShoutOut')

        s = ShoutOut(
            submitter=submitter,
            body=body,
            )

        s.save()

        User = get_user_model()

        # Find users in body with regexp
        found_users = re.findall(r'\@(\w+)\b', body)

        # Delete any existings mentions, as we intend to rebuild all mentions
        Mention = get_model('shoutouts', 'Mention')
        Mention.objects.filter(shoutout=s).delete()
        mention_count = 0

        # Create a mention for each found user if they really are a user
        for user in found_users:
            try:
                current_user = User.objects.get(username=user)
                Mention.objects.create(
                    shoutout=s,
                    user=current_user,
                )
                mention_count += 1
            except User.DoesNotExist:
                pass

        s.mention_count = mention_count
        s.save()

        return s




    def public(self):
        return self.get_queryset().public()

    def needs_approval(self):
        return self.get_queryset().needs_approval()