# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShoutOut'
        db.create_table(u'shoutouts_shoutout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submitter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shoutouts_submitted', to=orm['auth.User'])),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('approved_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='shoutouts_approved', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'shoutouts', ['ShoutOut'])

        # Adding model 'Mention'
        db.create_table(u'shoutouts_mention', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shoutout', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mentions', to=orm['shoutouts.ShoutOut'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shoutout_mentions', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'shoutouts', ['Mention'])


    def backwards(self, orm):
        # Deleting model 'ShoutOut'
        db.delete_table(u'shoutouts_shoutout')

        # Deleting model 'Mention'
        db.delete_table(u'shoutouts_mention')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'shoutouts.mention': {
            'Meta': {'object_name': 'Mention'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shoutout': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentions'", 'to': u"orm['shoutouts.ShoutOut']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shoutout_mentions'", 'to': u"orm['auth.User']"})
        },
        u'shoutouts.shoutout': {
            'Meta': {'object_name': 'ShoutOut'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'shoutouts_approved'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shoutouts_submitted'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['shoutouts']