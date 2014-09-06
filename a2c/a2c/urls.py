# from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'a2c.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# )


import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': os.path.join(BASE_DIR, 'media')}),
    url(r'', include('feincms.contrib.preview.urls')),
    url(r'', include('feincms.urls'))
) #+ staticfiles_urlpatterns()
