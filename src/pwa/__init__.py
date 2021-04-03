'''
Adds PWA functionality to the site, as well as some related extras.

Includes:
- manifest.json (loaded from static files)
- robots.txt (loaded from static files)
'''

from django.conf import settings as user_settings
from . import default_settings


class AppSettings:
    'Settings for the app - manages defaults'
    def __getattr__(self, name):
        if hasattr(user_settings, name):
            item = getattr(user_settings, name)
            if isinstance(item):
                base_item: dict = getattr(default_settings, name)
                base_item.update(item)
                return base_item
            return item
        if hasattr(default_settings, name):
            return getattr(default_settings, name)
        return getattr(user_settings, name)


settings = AppSettings()
__all__ = ['settings']
