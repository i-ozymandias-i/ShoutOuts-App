from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
#import regex
import re
from .managers import ShoutOutManager

# Create your models here.

class ShoutOut(models.Model):
    """
    ShoutOut Model
    Stores individual employee ShoutOuts for a job well done. Need moderator approval before
    being visible to non-moderators
    """

    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shoutouts_submitted')
    body = models.TextField()

    created = models.DateTimeField(default=timezone.now)

    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
    )

    approved = models.BooleanField(default=False, db_index=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='shoutouts_approved',
        blank=True,
        null=True,
    )

    mention_count = models.IntegerField(default=0)


    objects =  ShoutOutManager()



    def __unicode__(self):
        return "From {0} #{1}".format(
            self.submitter.username,
            self.pk,
        )

    def save(self, *args, **kwargs):
        if self.pk:
            self.modified = timezone.now()

        #save to DB
        super(ShoutOut, self).save(*args, **kwargs)
        
        #we have a real in the DB ShoutOut with mentions




class Mention(models.Model):
    """
    Model to track users that are mentioned in a shoutout
    """

    shoutout= models.ForeignKey(ShoutOut, related_name='mentions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shoutout_mentions')

    #This is a to-string method
    def __unicode__(self):
        return "ShoutOut {0} mentions User {1}".format(
            self.shoutout.pk,
            self.user.username,
        )