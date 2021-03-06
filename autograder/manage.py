#!/usr/bin/env python
'''
Last edited by: Eric Zair
Last edited on: 03/27/2019
'''
import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
    try:
        from django.core.management import execute_from_command_line
        # Added by: ERIC ZAIR
        # Load the fixtures that we have in our database
        # every time we run migrate command.
        # We do this so we can automatically load the fitxures for groups and users.
        #instead of having to do it after every migrate.
        
        # THIS WILL BE FIXED LATER, I GOT IT QQ QQ
        # if (len(sys.argv) == 2) and (sys.argv[1] == 'migrate'):
        #     execute_from_command_line(['manage.py', 'loaddata', 'fixtures/all_fixtures.json'])
        execute_from_command_line(sys.argv)
    
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)