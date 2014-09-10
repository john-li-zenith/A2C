from django.contrib import admin
from apps.models import AppCategory, App
from feincms.admin import tree_editor

# Register your models here.

class AppCategoryAdmin(tree_editor.TreeEditor):
    pass
        
class AppAdmin(admin.ModelAdmin):
    pass

admin.site.register(App,AppAdmin)
admin.site.register(AppCategory, AppCategoryAdmin)