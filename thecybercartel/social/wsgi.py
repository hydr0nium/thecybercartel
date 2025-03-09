"""
WSGI config for social project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from social.database_manager import init

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social.settings')
init()
application = get_wsgi_application()
