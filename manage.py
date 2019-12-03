#!/usr/bin/env python

import os
import sys
import django
from django.conf import settings

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "blog",
]


if __name__ == '__main__':
    # settings.configure(
    #     DATABASES={
    #         "default": {
    #             "ENGINE": "django.db.backends.sqlite3",
    #         }
    #     },
    #     INSTALLED_APPS=INSTALLED_APPS,
    #     ROOT_URLCONF="tests.urls",
    # )
    #
    os.environ.update({"DJANGO_SETTINGS_MODULE": "tests.settings"})
    # django.setup()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


