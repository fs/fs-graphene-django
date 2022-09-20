from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from django.utils.functional import SimpleLazyObject


class TestAuthenticationMiddleware:
    """Setup request with user."""

    def resolve(self, next_middleware, root, info, **kwargs):
        """Link user for request by django authentication."""
        context = info.context

        def get_user():
            return authenticate(request=context) or AnonymousUser()

        context.user = SimpleLazyObject(get_user)
        return next_middleware(root, info, **kwargs)
