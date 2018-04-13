#!/usr/bin/python
"""setup script for django_oidc_user."""
from setuptools import find_packages, setup

import django_oidc_user


setup(name='django-oidc-user',
      version=django_oidc_user.__version__,
      description='Django application for OIDC user authentication',
      packages=find_packages(),
      install_requires=['Django>=1.11'],
      extras_require={'quality': ['isort', 'flake8', 'pydocstyle']})
