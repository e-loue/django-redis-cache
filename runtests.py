#!/usr/bin/env python
import sys

from os.path import dirname, abspath

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=[
            'tests.testapp',
        ]
    )

from django.test.simple import run_tests


def runtests(*test_args):
    if not test_args:
        test_args = ['testapp']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])