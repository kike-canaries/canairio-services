#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import load_dotenv
from pathlib import Path

from shutil import copyfile

# Check dotenv
if not os.path.exists(Path('') / '.env'):
    copyfile(Path('') / 'example.env', Path('') / '.env')
# Load dotenv
load_dotenv(dotenv_path=Path('') / '.env')


def main():
    if os.getenv('DJANGO_SETTINGS_MODULE') is not None:
        DJANGO_SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE')
    else:
        DJANGO_SETTINGS_MODULE = 'api.settings.prod'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
