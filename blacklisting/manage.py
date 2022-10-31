#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blacklisting.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def startApp():
    if os.environ.get('RUN_MAIN') != 'true':
        ba="Blacklist Application"
        print(ba+ "Starting")
    else:
        print(ba+ "is Re-loading")


def endApp():
    print("Stopping the Application")


if __name__ == '__main__':
    startApp()
    main()
    endApp()
