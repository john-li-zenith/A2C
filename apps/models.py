from django.db import models
from mptt.models import MPTTModel
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from django import forms
from easy_thumbnails.fields import ThumbnailerImageField as thumbfield
from django_countries.fields import CountryField


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

class AppKey(models.Model):
    appkey=models.CharField(max_length=200)
    is_used=models.BooleanField()
    
    def __unicode__(self):
        return self.appkey
        
        
class App(models.Model):
    name=models.CharField(max_length=30)
    name_zh=models.CharField(verbose_name='Name in Chinese',max_length=30,blank=True,null=True,help_text='A chinese name for your app, if you dont have, we will create one that matches your app english name')
    description_short=models.TextField(verbose_name='Brief/Overview',null=True)
    description_long=models.TextField(verbose_name='Description',null=True)
    icon_512=thumbfield(upload_to='apps/icon/%Y/%m/%d',resize_source=dict(size=(512, 512), sharpen=True),null=True)
    icon_72=thumbfield(upload_to='apps/icon/%Y/%m/%d',resize_source=dict(size=(72, 72), sharpen=True),null=True)
    category=models.ForeignKey(AppCategory,blank=True, null=True)
    user=models.ForeignKey(User)
    appkey=models.CharField(max_length=100,blank=True,null=True)
    appfile = models.FileField(upload_to='apps/%Y/%m/%d',blank=True,null=True)
    screenshot_1=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d',null=True)
    screenshot_2=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d',null=True)
    screenshot_3=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d',null=True)
    screenshot_4=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d',null=True)
    screenshot_5=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d',null=True)
    screenshot_6=models.ImageField(verbose_name='Google Play Screenshot 1',upload_to='apps/screenshot/%Y/%m/%d',null=True)
    screenshot_7=models.ImageField(verbose_name='Google Play Screenshot 2',upload_to='apps/screenshot/%Y/%m/%d',null=True)
    screenshot_8=models.ImageField(verbose_name='Google Play Screenshot 3',upload_to='apps/screenshot/%Y/%m/%d',null=True)
    screenshot_9=models.ImageField(verbose_name='Google Play Screenshot 4',upload_to='apps/screenshot/%Y/%m/%d',null=True)
    screenshot_10=models.ImageField(verbose_name='Google Play Screenshot 5',upload_to='apps/screenshot/%Y/%m/%d',null=True)
    uploaded=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    
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
    
    # # return next unused app key, and mark it used    
    # def get_next_appkey(self):
    #     if not self.has_appkey:
    #         if AppKey.objects.filter(is_used=False)[0]:
    #             AppKey.objects.filter(is_used=False)[0].update(is_used=True)
    #             return AppKey.objects.filter(is_used=False)[0].appkey
    #         else:
    #             return None
    #     return None
        
    def __unicode__(self):
        return self.name

class AppUpdate(models.Model):
    app=models.ForeignKey(App)
    user=models.ForeignKey(User,blank=True,null=True)
    appfile=models.FileField(upload_to='apps/upgrade/%Y/%m/%d',blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    uploaded=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __unicode__(self):
        return 'Update for ' + self.app.name
    
class AppLogType(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name

class AppLog(models.Model):
    app=models.ForeignKey(App)
    type=models.ForeignKey(AppLogType,blank=True,null=True)
    description=models.TextField()
    image=models.ImageField(upload_to='apps/logs/%Y/%m/%d',blank=True,null=True)
    created=models.DateTimeField()
    
    def __unicode__(self):
        return unicode(self.created)
        
    
    
