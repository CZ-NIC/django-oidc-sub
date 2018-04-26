"""Unittests for backends."""
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from django_oidc_sub.backends import OidcSubBackend
from django_oidc_sub.models import OidcUserSub


@override_settings(OIDC_OP_AUTHORIZATION_ENDPOINT='http://example/oidc/authorization',
                   OIDC_OP_TOKEN_ENDPOINT='http://example/oidc/token',
                   OIDC_OP_USER_ENDPOINT='http://example/oidc/user',
                   OIDC_RP_CLIENT_ID='clientid',
                   OIDC_RP_CLIENT_SECRET='client_secret')
class TestOidcSubBackend(TestCase):
    """Unittests for OidcSubBackend."""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(username='test')
        cls.backend = OidcSubBackend()

    def test_no_user(self):
        self.assertEqual(len(self.backend.filter_users_by_claims({'sub': 'aaa'})), 0)

    def test_user(self):
        OidcUserSub.objects.create(sub='aaa', user=self.user)
        query = self.backend.filter_users_by_claims({'sub': 'aaa'})
        self.assertEqual(len(query), 1)
        self.assertEqual(query[0], self.user)
