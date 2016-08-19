# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RequestKeeperModel.is_viewed'
        db.delete_column(u'hello_requestkeepermodel', 'is_viewed')

        # Deleting field 'RequestKeeperModel.path'
        db.delete_column(u'hello_requestkeepermodel', 'path')

        # Adding field 'RequestKeeperModel.name'
        db.add_column(u'hello_requestkeepermodel', 'name',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'RequestKeeperModel.status'
        db.add_column(u'hello_requestkeepermodel', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=3),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'RequestKeeperModel.is_viewed'
        db.add_column(u'hello_requestkeepermodel', 'is_viewed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'RequestKeeperModel.path'
        raise RuntimeError("Cannot reverse this migration. 'RequestKeeperModel.path' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'RequestKeeperModel.path'
        db.add_column(u'hello_requestkeepermodel', 'path',
                      self.gf('django.db.models.fields.CharField')(max_length=1024),
                      keep_default=False)

        # Deleting field 'RequestKeeperModel.name'
        db.delete_column(u'hello_requestkeepermodel', 'name')

        # Deleting field 'RequestKeeperModel.status'
        db.delete_column(u'hello_requestkeepermodel', 'status')


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
        },
        u'hello.requestkeepermodel': {
            'Meta': {'object_name': 'RequestKeeperModel'},
            'author': ('django.db.models.fields.CharField', [], {'default': "'anonymous'", 'max_length': '256'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6'}),
            'name': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '3'})
        }
    }

    complete_apps = ['hello']