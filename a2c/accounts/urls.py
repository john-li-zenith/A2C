from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
#from accounts.views import ContactCreateView


urlpatterns = patterns(
    '',
     url('^dash/$','accounts.views.account_dash',name='dash'),
     url(r'^info/$', 'accounts.views.contact_update', name='contact_update'),
     url('^thankyou/$','accounts.views.thankyou',name='thankyou'),
    )