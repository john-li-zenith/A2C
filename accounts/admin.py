from django.contrib import admin
from accounts.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('user',)


admin.site.register(Contact,ContactAdmin)
