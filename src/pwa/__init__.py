'''
Adds PWA functionality to the site, as well as some related extras.

Includes:
- manifest.json (loaded from static files)
- robots.txt (loaded from static files)
'''

from django.conf import settings as user_settings
from . import default_settings


class AppSettings:
    def __getattr__(self, name):
        if hasattr(user_settings, name):
            return getattr(user_settings, name)
        if hasattr(default_settings, name):
            return getattr(default_settings, name)
        return getattr(user_settings, name)


settings = AppSettings()
__all__ = ['settings']
