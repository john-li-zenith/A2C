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
    appkey=models.CharField(max_length=100,blank=True,null=True)
    appfile = models.FileField(upload_to='apps/'+user.id+'/%Y/%m/%d')
    uploaded=models.DateTimeField(auto_now_add=True)
    
    def has_appkey(self):
        if self.appkey:
            return True
        return False
    
    def get_category(self):
        return self.category
        
    def get_user_id(self):
        return self.user.id
        
    def get_user(self):
        return '%s %s' % (self.user.first_name,self.user.last_name)
        
    def __unicode__(self):
        return self.name
    
class AppForm(ModelForm):
    class Meta:
        model = App
        fields = ['name', 'description', 'category', 'appfile']
        
class AppKey(models.Model):
    appkey=models.CharField(max_length=200)
    is_used=models.BooleanField()
    
    def __unicode__(self):
        return self.appkey