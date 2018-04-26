# django-oidc-sub

[![Build Status](https://travis-ci.org/tpazderka/django-oidc-sub.svg?branch=master)](https://travis-ci.org/tpazderka/django-oidc-sub)
[![codecov](https://codecov.io/gh/tpazderka/django-oidc-sub/branch/master/graph/badge.svg)](https://codecov.io/gh/tpazderka/django-oidc-sub)

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

1. Add ``django_oidc_sub`` and ``mozilla_django_oidc`` to your installed apps.
2. Add ``django_oidc_sub.backends.OidcSubBackend`` to your ``AUTHENTICATION_BACKENDS``.

## Testing

```
tox
```

## License

See [LICENSE](LICENSE)
