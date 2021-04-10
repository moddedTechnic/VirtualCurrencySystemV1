'''A replacement for the builtin startapp command, to allow adding multipl apps
at once.
'''

from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from django.core.management.commands import startapp


class Command(BaseCommand):
    'The command class'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_app = startapp.Command(*args, **kwargs)

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'names', nargs='+', help='Name of the application or project.')
        parser.add_argument(
            '--template', help='The path or URL to load the template from.')
        parser.add_argument(
            '--extension', '-e', dest='extensions',
            action='append', default=['py'],
            help='The file extension(s) to render (default: "py"). '
                 'Separate multiple extensions with commas, or use '
                 '-e multiple times.'
        )
        parser.add_argument(
            '--name', '-n', dest='files',
            action='append', default=[],
            help='The file name(s) to render. Separate multiple file names '
                 'with commas, or use -n multiple times.'
        )

    def handle(self, *args, **options):
        kwargs = options.copy()
        del kwargs['names']
        for name in options['names']:
            kwargs['name'] = name
            self.start_app.handle(*args, **kwargs)
