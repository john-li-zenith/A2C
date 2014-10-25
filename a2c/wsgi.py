"""
WSGI config for a2c project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
from django.conf import settings

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "a2c.settings")

if not settings.DEBUG:
    from django.core.wsgi import get_wsgi_application
    from dj_static import Cling

    application = Cling(get_wsgi_application())
    
if settings.DEBUG:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()