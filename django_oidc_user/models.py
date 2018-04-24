"""Model for storing sub and User."""
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class OidcUserSub(models.Model):
    """Store user and sub."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='oidc_subs', on_delete=models.CASCADE)
    sub = models.TextField(unique=True)
