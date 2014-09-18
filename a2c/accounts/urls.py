from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
     url(r'^info/$', 'accounts.views.contact_update', name='contact_update'),
    )