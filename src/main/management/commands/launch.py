'''
A custom launch command.
Almost identical to runserver except watches some additional files.

Watched files:
- static/*.json
- static/**/index.json

Note: it would ideally watch all json files not in node modules, but
        it didn't seem to want to find the correct files
'''

import os
import signal
import sys
from pathlib import Path

from django.core.management.commands import runserver
from django.utils import autoreload

def _run_with_reloader(main_func, *args, **kwargs):
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    try:
        if os.environ.get(autoreload.DJANGO_AUTORELOAD_ENV) == 'true':
            reloader = autoreload.get_reloader()
            # reloader.watch_dir()
            path = Path(__file__).parent.parent.parent.parent / 'static'
            reloader.watch_dir(path, '*.json')
            reloader.watch_dir(path, '**/index.json')
            autoreload.logger.info(
                'Watching for file changes with %s', reloader.__class__.__name__
            )
            autoreload.start_django(reloader, main_func, *args, **kwargs)
        else:
            exit_code = autoreload.restart_with_reloader()
            sys.exit(exit_code)
    except KeyboardInterrupt:
        pass


class Command(runserver.Command):
    def run(self, **options):
        '''Run the server, using the autoreloader if needed.'''
        use_reloader = options['use_reloader']

        if use_reloader:
            _run_with_reloader(self.inner_run, **options)
        else:
            self.inner_run(None, **options)