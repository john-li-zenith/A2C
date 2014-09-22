from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
     url('^dash/$','accounts.views.account_dash',name='dash'),
     url(r'^info/$', 'accounts.views.contact_update', name='contact_update'),
    )