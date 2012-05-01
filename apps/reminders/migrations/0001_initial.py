# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reminder'
        db.create_table('reminders_reminder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 5, 1, 0, 0), blank=True)),
            ('datetime_expire', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('reminders', ['Reminder'])

        # Adding model 'Participant'
        db.create_table('reminders_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reminder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reminders.Reminder'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('reminders', ['Participant'])

        # Adding unique constraint on 'Participant', fields ['reminder', 'user', 'role']
        db.create_unique('reminders_participant', ['reminder_id', 'user_id', 'role'])

        # Adding model 'Notification'
        db.create_table('reminders_notification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reminder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reminders.Reminder'])),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reminders.Participant'])),
            ('preemptive', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('reminders', ['Notification'])

    def backwards(self, orm):
        # Removing unique constraint on 'Participant', fields ['reminder', 'user', 'role']
        db.delete_unique('reminders_participant', ['reminder_id', 'user_id', 'role'])

        # Deleting model 'Reminder'
        db.delete_table('reminders_reminder')

        # Deleting model 'Participant'
        db.delete_table('reminders_participant')

        # Deleting model 'Notification'
        db.delete_table('reminders_notification')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'reminders.notification': {
            'Meta': {'object_name': 'Notification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reminders.Participant']"}),
            'preemptive': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'reminder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reminders.Reminder']"})
        },
        'reminders.participant': {
            'Meta': {'unique_together': "(('reminder', 'user', 'role'),)", 'object_name': 'Participant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reminder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reminders.Reminder']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'reminders.reminder': {
            'Meta': {'ordering': "('-datetime_created',)", 'object_name': 'Reminder'},
            'datetime_created': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 5, 1, 0, 0)', 'blank': 'True'}),
            'datetime_expire': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['reminders']