# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'LifeEntry.date'
        db.delete_column('entries_lifeentry', 'date')

        # Adding field 'LifeEntry.date_written'
        db.add_column('entries_lifeentry', 'date_written',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 4, 19, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'LifeEntry.about_date'
        db.add_column('entries_lifeentry', 'about_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 4, 19, 0, 0)),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'LifeEntry.date'
        db.add_column('entries_lifeentry', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 4, 19, 0, 0)),
                      keep_default=False)

        # Deleting field 'LifeEntry.date_written'
        db.delete_column('entries_lifeentry', 'date_written')

        # Deleting field 'LifeEntry.about_date'
        db.delete_column('entries_lifeentry', 'about_date')

    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'entries.lifeentry': {
            'Meta': {'object_name': 'LifeEntry'},
            'about_date': ('django.db.models.fields.DateField', [], {}),
            'date_written': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['entries']