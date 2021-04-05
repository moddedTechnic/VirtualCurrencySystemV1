'''
Default values for the custom PWA settings
'''

LOAD_SERVICE_WORKER = False

MANIFEST = False
MANIFEST_DATA = {
    'filename': 'manifest.json',
    'use_file': True,
    'icons_path': '/icons',
    'icons': [],
    'start_url': '/',
    'scope': '/',
    'background_color': '#ffffff',
    'theme_color': '#000000',
    'display': 'standalone',
    'shortcuts': [],
    'screenshots': []
}
MANIFEST_FILE = False

ROBOTS = False
ROBOTS_DATA = {}
ROBOTS_FILE = False
