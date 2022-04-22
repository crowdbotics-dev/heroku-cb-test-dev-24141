"""
WSGI config for heroku_cb_test_dev_24141 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heroku_cb_test_dev_24141.settings')

application = get_wsgi_application()
