from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

User = get_user_model()


class TestIdAuthenticationBackend(BaseBackend):
    """Test authentication backend."""

    def authenticate(self, request=None, **kwargs):
        """Authentication by id in headers. Only for test authentication."""
        if request is None:
            return None

        user_id = request.META.get('USER_ID')
        users_qs = User.objects.filter(id=user_id)

        if users_qs.exists():
            return users_qs.get()

        return None
