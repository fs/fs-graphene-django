from functools import wraps

from server.core.auth.jwt.exceptions import PermissionDenied

try:
    import django_filters  # noqa

    DJANGO_FILTER_INSTALLED = True
except ImportError:
    DJANGO_FILTER_INSTALLED = False


try:
    import django_filters  # noqa

    DJANGO_POLYMORPHIC_INSTALLED = True
except ImportError:
    DJANGO_POLYMORPHIC_INSTALLED = False
