# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'SignupRequest.referred_by'
        db.add_column('launch_signuprequest', 'referred_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['launch.SignupRequest'], null=True, blank=True), keep_default=False)

        # Adding unique constraint on 'SignupRequest', fields ['email']
        db.create_unique('launch_signuprequest', ['email'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'SignupRequest', fields ['email']
        db.delete_unique('launch_signuprequest', ['email'])

        # Deleting field 'SignupRequest.referred_by'
        db.delete_column('launch_signuprequest', 'referred_by_id')


    models = {
        'launch.signuprequest': {
            'Meta': {'object_name': 'SignupRequest'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'referred_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['launch.SignupRequest']", 'null': 'True', 'blank': 'True'}),
            'signed_up': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['launch']
