from django.test import TestCase
from apps.models import AppCategory,App
# Create your tests here.

class AppsTestCase(TestCase):
    """Test Case for apps, including models tests, views tests, etc.
    instructions need to added here if i have time ( :"""
    def setUp(self):
        cat1=AppCategory.objects.create(name="Social",slug="social")
        cat2=AppCategory.objects.create(name="messenger",slug="messenger",parent=self.cat1)
        App.objects.create()