from functools import wraps
from typing import Any, Callable, TypeVar, cast

from graphene_django_pretty.auth.exceptions import PermissionDeniedError

FuncT = TypeVar('FuncT', bound=Callable[..., Any])


def check_permissions(info, input_, permission_classes) -> None:  # noqa: WPS110
    """Running all permissions classes in mutations."""
    for permission in permission_classes:
        if not permission.has_permissions(info, input_):
            raise PermissionDeniedError()


def decorate_mutate_func(mutate_func, permission_classes) -> FuncT:
    """Adding check user permissions before mutate."""

    @wraps(mutate_func)
    def wrapper(_, info, **kwargs):  # noqa: WPS110
        input_ = kwargs.get('input', {})
        check_permissions(info, input_, permission_classes=permission_classes)
        return mutate_func(info, input_)

    return cast(FuncT, wrapper)
