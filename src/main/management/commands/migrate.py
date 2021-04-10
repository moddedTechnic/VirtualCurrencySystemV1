'Run `makemigrations` followed by `migrate`'

from django.core import management
from django.core.management.base import CommandParser
from django.core.management.commands import migrate, makemigrations
from django.db.utils import DEFAULT_DB_ALIAS


class Command(management.BaseCommand):
    'The command class'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.make_migrations = makemigrations.Command(*args, **kwargs)
        self.migrate = migrate.Command(*args, **kwargs)

    def add_arguments(self, parser: CommandParser) -> None:
        # region makemigrations
        parser.add_argument(
            'args', metavar='app_label', nargs='*',
            help='Specify the app label(s) to create migrations for.',
        )
        parser.add_argument(
            '--dry-run', action='store_true',
            help='Just show what migrations would be made; don\'t actually '
                'write them.',
        )
        parser.add_argument(
            '--merge', action='store_true',
            help='Enable fixing of migration conflicts.',
        )
        parser.add_argument(
            '--empty', action='store_true',
            help='Create an empty migration.',
        )
        parser.add_argument(
            '--noinput', '--no-input', action='store_false', dest='interactive',
            help='Tells Django to NOT prompt the user for input of any kind.',
        )
        parser.add_argument(
            '-n', '--name',
            help='Use this name for migration file(s).',
        )
        parser.add_argument(
            '--no-header', action='store_false', dest='include_header',
            help='Do not add header comments to new migration file(s).',
        )
        parser.add_argument(
            '--check', action='store_true', dest='check_changes',
            help='Exit with a non-zero status if model changes are missing '
                'migrations.',
        )
        # endregion

        # region migrate
        parser.add_argument(
            'app_label', nargs='?',
            help='App label of an application to synchronize the state.',
        )
        parser.add_argument(
            'migration_name', nargs='?',
            help='Database state will be brought to the state after that '
                 'migration. Use the name \'zero\' to unapply all migrations.',
        )
        parser.add_argument(
            '--database',
            default=DEFAULT_DB_ALIAS,
            help='Nominates a database to synchronize. Defaults to the '
                '\'default\' database.',
        )
        parser.add_argument(
            '--fake', action='store_true',
            help='Mark migrations as run without actually running them.',
        )
        parser.add_argument(
            '--fake-initial', action='store_true',
            help='Detect if tables already exist and fake-apply initial '
                'migrations if so. Make sure that the current database schema '
                'matches your initial migration before using this flag. Django'
                ' will only check for an existing table name.',
        )
        parser.add_argument(
            '--plan', action='store_true',
            help='Shows a list of the migration actions that will be performed.',
        )
        parser.add_argument(
            '--run-syncdb', action='store_true',
            help='Creates tables for apps without migrations.',
        )
        # endregion

    def handle(self, *args, **options):
        options['check_unapplied'] = options['check_changes']
        self.make_migrations.handle(*args, **options)
        self.migrate.handle(*args, **options)
