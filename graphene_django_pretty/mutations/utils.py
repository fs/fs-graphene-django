from functools import wraps

from fs_graphene_django.auth.exceptions import PermissionDeniedError


def check_permissions(info, input_, permission_classes):
    """Running all permissions classes in mutations."""
    for permission in permission_classes:
        if not permission.has_permissions(info, input_):
            raise PermissionDeniedError()


def decorate_mutate_func(mutate_func, permission_classes):
    """Adding check user permissions before mutate."""

    @wraps(mutate_func)
    def wrapper(_, info, **kwargs):
        input_ = kwargs.get('input', {})
        check_permissions(info, input_, permission_classes=permission_classes)
        return mutate_func(info, input_)

    return wrapper
