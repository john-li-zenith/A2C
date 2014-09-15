from django.contrib import admin
from accounts.models import Contact, CreditCard

class ContactAdmin(admin.ModelAdmin):
    pass

class CreditCardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact,ContactAdmin)
admin.site.register(CreditCard,CreditCardAdmin)