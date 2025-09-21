#!/usr/bin/env python
"""
Django management script for the ecommerce project.

This script serves as the entry point for Django's command-line interface,
providing utilities for administrative tasks such as running the development
server, creating and applying database migrations, managing applications,
and other Django management commands.

Usage: python manage.py <command> [options]
For a list of available commands, run: python manage.py help
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
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
