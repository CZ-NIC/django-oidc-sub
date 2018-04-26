#!/usr/bin/python
"""setup script for django_oidc_sub."""
from setuptools import find_packages, setup

import django_oidc_sub


setup(name='django-oidc-sub',
      version=django_oidc_sub.__version__,
      description='Django application for OIDC user authentication',
      long_description=open('README.md').read(),
      author='Tomas Pazderka',
      author_email='tomas.pazderka@nic.cz',
      url='https://github.com/tpazderka/django-oidc-sub',
      packages=find_packages(),
      install_requires=['Django>=1.11', 'mozilla-django-oidc'],
      extras_require={'quality': ['isort', 'flake8', 'pydocstyle']})
