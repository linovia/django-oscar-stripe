#!/usr/bin/env python
"""
setup
~~~~~

:copyright: (c) 2014 by Xavier Ordoquy,
see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


tests_require = [
    'pytest',
    'pytest-cov>=1.4',
    'pytest-django',
]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='django-oscar-stripe',
    version='0.1.0',
    author='Xavier Ordoquy',
    author_email='xordoquy@linovia.com',

    url='https://github.com/linovia/django-oscar-stripe',
    description='',
    long_description=open('README.md').read(),
    license='BSD',

    packages=[
        'django-oscar-stripe',
    ],
    package_dir={
        'django-oscar-stripe': 'django-oscar-stripe'
    },
    zip_safe=False,

    install_requires=[
        'django-oscar>=0.6',
    ],
    include_package_data=True,

    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],

    cmdclass={'test': PyTest},
    tests_require=tests_require,
    extras_require={
        'tests': tests_require,
    },
)
