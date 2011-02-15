# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'SignupRequest.ip_address'
        db.add_column('launch_signuprequest', 'ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'SignupRequest.ip_address'
        db.delete_column('launch_signuprequest', 'ip_address')


    models = {
        'launch.signuprequest': {
            'Meta': {'object_name': 'SignupRequest'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'referred_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['launch.SignupRequest']", 'null': 'True', 'blank': 'True'}),
            'signed_up': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['launch']
