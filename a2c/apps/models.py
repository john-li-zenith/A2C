from django.db import models
from mptt.models import MPTTModel
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm
from easy_thumbnails.fields import ThumbnailerImageField as thumbfield


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
    name_zh=models.CharField(max_length=30,blank=True,null=True,help_text='A chinese name for your app, if you dont have, we will create one that matches your app english name')
    description_short=models.TextField()
    description_long=models.TextField()
    icon_512=thumbfield(upload_to='apps/icon/%Y/%m/%d',resize_source=dict(size=(512, 512), sharpen=True))
    icon_72=thumbfield(upload_to='apps/icon/%Y/%m/%d',resize_source=dict(size=(72, 72), sharpen=True))
    category=models.ForeignKey(AppCategory,blank=True, null=True)
    user=models.ForeignKey(User)
    appkey=models.CharField(max_length=100,blank=True,null=True)
    appfile = models.FileField(upload_to='apps/%Y/%m/%d')
    screenshot_1=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d')
    screenshot_2=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d')
    screenshot_3=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d')
    screenshot_4=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d')
    screenshot_5=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d')
    screenshot_6=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d')
    screenshot_7=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d')
    screenshot_8=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d')
    screenshot_9=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d')
    screenshot_10=models.ImageField(upload_to='apps/screenshot/%Y/%m/%d')
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
    
class AppForm(ModelForm):
    class Meta:
        model = App
        fields = ['name','name_zh','description_short','description_long', 'icon_512','icon_72', 'appfile','screenshot_1'
        ,'screenshot_2','screenshot_3','screenshot_4','screenshot_5','screenshot_6','screenshot_7','screenshot_3','screenshot_9','screenshot_10']