from django.db import models
from mptt.models import MPTTModel
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.


@python_2_unicode_compatible
class AppCategory(MPTTModel):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='children')

    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name = 'App_Category'
        verbose_name_plural = 'App_Categories'

    def __str__(self):
        return self.name
        
class App(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    category=models.ForeignKey(AppCategory,blank=True, null=True)
    user=models.ForeignKey(User)
    appfile = models.FileField(upload_to='apps/%Y/%m/%d')
    
    
class AppForm(ModelForm):
    class Meta:
        model = App
        fields = ['name', 'description', 'category', 'appfile']