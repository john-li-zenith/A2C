# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AppCategory'
        db.create_table(u'apps_appcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['apps.AppCategory'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'apps', ['AppCategory'])

        # Adding model 'AppKey'
        db.create_table(u'apps_appkey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appkey', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('is_used', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'apps', ['AppKey'])

        # Adding model 'App'
        db.create_table(u'apps_app', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_zh', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('description_short', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_long', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('icon_512', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('icon_72', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.AppCategory'], null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('appkey', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('appfile', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('screenshot_1', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('screenshot_2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('screenshot_3', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('screenshot_4', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('screenshot_5', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('screenshot_6', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('screenshot_7', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('screenshot_8', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('screenshot_9', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('screenshot_10', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('allow_to_upload', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'apps', ['App'])

        # Adding model 'AppUpdate'
        db.create_table(u'apps_appupdate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.App'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('appfile', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'apps', ['AppUpdate'])

        # Adding model 'AppLog'
        db.create_table(u'apps_applog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.App'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'apps', ['AppLog'])


    def backwards(self, orm):
        # Deleting model 'AppCategory'
        db.delete_table(u'apps_appcategory')

        # Deleting model 'AppKey'
        db.delete_table(u'apps_appkey')

        # Deleting model 'App'
        db.delete_table(u'apps_app')

        # Deleting model 'AppUpdate'
        db.delete_table(u'apps_appupdate')

        # Deleting model 'AppLog'
        db.delete_table(u'apps_applog')


    models = {
        u'apps.app': {
            'Meta': {'object_name': 'App'},
            'allow_to_upload': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'appfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'appkey': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.AppCategory']", 'null': 'True', 'blank': 'True'}),
            'description_long': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_short': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icon_512': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'icon_72': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'screenshot_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'screenshot_10': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'screenshot_2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'screenshot_3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'screenshot_4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'screenshot_5': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'screenshot_6': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'screenshot_7': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'screenshot_8': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'screenshot_9': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'apps.appcategory': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'AppCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['apps.AppCategory']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'apps.appkey': {
            'Meta': {'object_name': 'AppKey'},
            'appkey': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_used': ('django.db.models.fields.BooleanField', [], {})
        },
        u'apps.applog': {
            'Meta': {'object_name': 'AppLog'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.App']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'apps.appupdate': {
            'Meta': {'object_name': 'AppUpdate'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.App']"}),
            'appfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
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
        }
    }

    complete_apps = ['apps']