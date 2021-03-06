"""
WSGI config for audioclassweekly project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/ferin_mac/bssmsharerecords/audioclassweekly')

sys.path.append('/home/ferin_mac/bssmsharerecords/venv/lib/python3.8/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'audioclassweekly.settings')

application = get_wsgi_application()
