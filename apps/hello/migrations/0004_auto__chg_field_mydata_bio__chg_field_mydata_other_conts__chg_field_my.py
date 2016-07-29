# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MyData.bio'
        db.alter_column(u'hello_mydata', 'bio', self.gf('django.db.models.fields.TextField')(max_length=256, null=True))

        # Changing field 'MyData.other_conts'
        db.alter_column(u'hello_mydata', 'other_conts', self.gf('django.db.models.fields.TextField')(max_length=256, null=True))

        # Changing field 'MyData.email'
        db.alter_column(u'hello_mydata', 'email', self.gf('django.db.models.fields.EmailField')(max_length=30))

        # Changing field 'MyData.jabber'
        db.alter_column(u'hello_mydata', 'jabber', self.gf('django.db.models.fields.EmailField')(max_length=30))

    def backwards(self, orm):

        # Changing field 'MyData.bio'
        db.alter_column(u'hello_mydata', 'bio', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'MyData.other_conts'
        db.alter_column(u'hello_mydata', 'other_conts', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'MyData.email'
        db.alter_column(u'hello_mydata', 'email', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'MyData.jabber'
        db.alter_column(u'hello_mydata', 'jabber', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'hello.mydata': {
            'Meta': {'object_name': 'MyData'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'other_conts': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['hello']