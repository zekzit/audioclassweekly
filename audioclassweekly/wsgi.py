"""
WSGI config for audioclassweekly project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys
#add path to django project folder
#sys.path.append('<PATH>/audioclassweekly')

#add virtualenv sit-packages path
#sys.path.append('<PATH_TO_VENV>/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'audioclassweekly.settings')

application = get_wsgi_application()
