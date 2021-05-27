'Command to watch and compile SASS and SCSS files'

import os
from pathlib import Path
import signal
import sys

from django.core.management import BaseCommand
from django.utils import autoreload

from main import settings
from utils import scss


def _run_with_reloader(main_func, *args, **kwargs):
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    try:
        if os.environ.get(autoreload.DJANGO_AUTORELOAD_ENV) == 'true':
            reloader = autoreload.StatReloader()
            # reloader.watch_dir()
            for item in settings.STATICFILES_DIRS:
                scss_dir = item / 'scss'
                if scss_dir.exists():
                    reloader.watch_dir(scss_dir, '**/*.scss')
            autoreload.logger.info(
                'Watching for file changes with %s', reloader.__class__.__name__
            )
            autoreload.start_django(reloader, main_func, *args, **kwargs)
        else:
            exit_code = autoreload.restart_with_reloader()
            sys.exit(exit_code)
    except KeyboardInterrupt:
        pass


class Command(BaseCommand):
    'The command class'

    def add_arguments(self, parser):
        parser.add_argument(
            '--nothreading', action='store_false', dest='use_threading',
            help='Tells Django to NOT use threading.',
        )
        parser.add_argument(
            '--noreload', action='store_false', dest='use_reloader',
            help='Tells Django to NOT use the auto-reloader.',
        )

    def handle(self, **options):
        '''Run the server, using the autoreloader if needed.'''
        use_reloader = options.get('use_reloader', True)

        if use_reloader:
            _run_with_reloader(self.run, **options)
        else:
            self.run(None, **options)

    def run(self, *args, **options):
        for directory in settings.STATICFILES_DIRS:
            scss_dir: Path = directory / 'scss'
            if not scss_dir.exists():
                continue
            css_dir: Path = directory / 'css'
            for scss_file in scss_dir.glob('**/*.scss'):
                if scss_file.name.startswith('_'):
                    continue
                css_file = css_dir / scss_file.relative_to(scss_dir)
                if not css_file.parent.exists():
                    css_file.parent.mkdir()
                scss.compile(scss_file)
