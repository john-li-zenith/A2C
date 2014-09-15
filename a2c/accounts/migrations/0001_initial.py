# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'accounts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('gmail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('gmail_pw', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('company_or_team', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('business_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('business_license', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('license_scan_hand', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('license_scan_stamp', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('passport', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('passport_scan', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('passport_scan_hand', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('company_address', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'accounts', ['Contact'])

        # Adding model 'CreditCard'
        db.create_table(u'accounts_creditcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name_on_card', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('card_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('expiry_date', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('card_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'accounts', ['CreditCard'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'accounts_contact')

        # Deleting model 'CreditCard'
        db.delete_table(u'accounts_creditcard')


    models = {
        u'accounts.contact': {
            'Meta': {'object_name': 'Contact'},
            'business_license': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'company_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company_or_team': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gmail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'gmail_pw': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'license_scan_hand': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'license_scan_stamp': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'passport': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'passport_scan': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'passport_scan_hand': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'accounts.creditcard': {
            'Meta': {'object_name': 'CreditCard'},
            'card_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'card_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'expiry_date': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_on_card': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
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

    complete_apps = ['accounts']