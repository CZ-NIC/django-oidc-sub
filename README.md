# django-oidc-user

[![Build Status](https://travis-ci.org/tpazderka/django-oidc-user.svg?branch=master)](https://travis-ci.org/tpazderka/django-oidc-user)
[![codecov](https://codecov.io/gh/tpazderka/django-oidc-user/branch/master/graph/badge.svg)](https://codecov.io/gh/tpazderka/django-oidc-user)

> Django application for login through OpenID Connect

This library provides a database model for connection between ``AUTH_USER_MODEL`` and ``sub`` claim received from provider.
It also provides an authentication backend that returns appropriate User based on the received ``sub`` claim.

## Table of Contents
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Testint](#testing)
- [License](#license)

## Dependencies

- Django >=1.11
- mozilla-django-oidc

## Configuration

1. Add ``django_oidc_user`` and ``mozilla_django_oidc`` to your installed apps.
2. Add ``django_oidc_user.backends.OidcSubBackend`` to your ``AUTHENTICATION_BACKENDS``.

## Testing

```
tox
```

## License

See [LICENSE](LICENSE)
