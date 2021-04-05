'''
Default values for the custom PWA settings
'''

from pathlib import Path

static_path = Path(__file__).parent.parent / 'static'
RELOAD_ITEMS = [
    (static_path, '*.json'),
    (static_path, '**/index.json')
]

MIME_TYPES = {
    'js': 'application/javascript',
    'json': 'application/json',

    'css': 'text/css',
    'html': 'text/html',
    'txt': 'text/plain',

    'png': 'image/png',

    'ttf': 'font/ttf',
    'woff': 'font/woff',
    'woff2': 'font/woff2',
}
