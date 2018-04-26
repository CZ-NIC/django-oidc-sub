"""Authentication backends."""
from __future__ import unicode_literals

from mozilla_django_oidc.auth import OIDCAuthenticationBackend


class OidcSubBackend(OIDCAuthenticationBackend):
    """Backend for user Authentication."""

    def filter_users_by_claims(self, claims):
        """Retrieve user from sub."""
        return self.UserModel.objects.filter(oidc_subs__sub=claims['sub'])
