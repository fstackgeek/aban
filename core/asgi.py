"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

env = (os.environ.get('ENV') or 'DEVELOPMENT').lower()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'core.settings.{env}')

application = get_asgi_application()
