'''
Default values for the custom PWA settings
'''

from pathlib import Path

static_path = Path(__file__).parent.parent / 'static'
RELOAD_ITEMS = [
    (static_path, '*.json'),
    (static_path, '**/index.json')
]
