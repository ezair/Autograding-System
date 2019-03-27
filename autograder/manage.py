#!/usr/bin/env python
import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
    try:
        from django.core.management import execute_from_command_line
        # Added by: ERIC ZAIR
        # Load the fixtures that we have in our database
        # every time we run manage command.
        # We do this so we can automatically load the fitxures
        # instead of having to do it after every migrate.
        if (len(sys.argv) == 2) and (sys.argv[1] == 'migrate'):
            execute_from_command_line(['manage.py', 'loaddata', 'fixtures/group_fixtures.json'])
        execute_from_command_line(sys.argv)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)