from django.contrib import admin
from apps.models import AppCategory, App,AppKey,AppLog, AppUpdate, AppLogType
from feincms.admin import tree_editor

# Register your models here.

class AppCategoryAdmin(tree_editor.TreeEditor):
    pass

class AppLogTypeAdmin(admin.ModelAdmin):
    pass
        
class AppAdmin(admin.ModelAdmin):
    list_display = ('name','user')
    list_filter = ['user',]
    search_fields = ['name',]

class AppKeyAdmin(admin.ModelAdmin):
    pass

class AppLogAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created'
    list_display = ('description','created','app')
    ordering=('-created',)
    list_filter=('app',)
    
class AppUpdateAdmin(admin.ModelAdmin):
    pass

admin.site.register(AppLog,AppLogAdmin)
admin.site.register(App,AppAdmin)
admin.site.register(AppCategory, AppCategoryAdmin)
admin.site.register(AppKey,AppKeyAdmin)
admin.site.register(AppUpdate,AppUpdateAdmin)
admin.site.register(AppLogType,AppLogTypeAdmin)