from django.utils.translation import gettext_lazy as _

from fs_graphene_django.error.exceptions import GrapheneDjangoError


class PermissionDeniedError(GrapheneDjangoError):
    """Raises with unauthorized user."""

    message = _('You do not have permission to perform this action')
