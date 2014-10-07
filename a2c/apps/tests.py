from django.test import TestCase
from apps.models import AppCategory,App,AppKey
from django.contrib.auth.models import User
from datetime import datetime
from django.test.client import Client

# Create your tests here.

class AppsTestCase(TestCase):
    """Test Case for apps, including models tests, views tests, etc.
    instructions need to be added here if i have time ( :"""
    def setUp(self):
        self.client = Client()
        self.zenith=User.create_user('zenith', email=None, password='zenith',)
        self.cat1=AppCategory.objects.create(name="Social",slug="social")
        self.cat2=AppCategory.objects.create(name="messenger",slug="messenger",parent=self.cat1)
        self.appkey1=AppKey.objects.create(appkey='ABCDEFG',is_used=False)
        self.appkey2=AppKey.objects.create(appkey='HIJKLMN',is_used=False)
        
# Models test

    def test_create_app_instance(self):
        App.objects.create(name='Social King',description='A social app',category=self.cat2,user=self.zenith,)