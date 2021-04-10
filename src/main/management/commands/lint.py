'Command to run pylint'

import subprocess
from pathlib import Path

from django.conf import settings
from django.core.management import BaseCommand


class Command(BaseCommand):
    'The command class'

    def handle(self, *args, **options) -> None:
        base_dir: Path = settings.BASE_DIR
        directories = [
            item.relative_to(base_dir) for item in base_dir.glob('*')
            if item.is_dir()
        ]
        command = 'pylint --rcfile=..\\pylintrc'.split(' ') + directories
        proc = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.stdout: self.stdout.write(proc.stdout.read().decode('utf-8'))
        if proc.stderr: self.stderr.write(proc.stderr.read().decode('utf-8'))
