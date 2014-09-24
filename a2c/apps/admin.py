from django.contrib import admin
from apps.models import AppCategory, App,AppKey,AppLog
from feincms.admin import tree_editor

# Register your models here.

class AppCategoryAdmin(tree_editor.TreeEditor):
    pass
        
class AppAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['user',]
    search_fields = ['name',]

class AppKeyAdmin(admin.ModelAdmin):
    pass

class AppLogAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created'
    list_display = ('description','created','app')
    ordering=('-created',)
    list_filter=('app',)

admin.site.register(AppLog,AppLogAdmin)
admin.site.register(App,AppAdmin)
admin.site.register(AppCategory, AppCategoryAdmin)
admin.site.register(AppKey,AppKeyAdmin)