from django.utils.translation import gettext_lazy as _

from graphene_django_pretty.error.exceptions import GrapheneDjangoError


class PermissionDeniedError(GrapheneDjangoError):
    """Raises with unauthorized user."""

    default_message = _('You do not have permission to perform this action')
