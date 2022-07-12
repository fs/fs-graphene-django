from enum import Enum
from functools import wraps
from typing import List

from graphene_django_pretty.auth.exceptions import PermissionDeniedError


def get_enum_list_as_input(args: List) -> List[str]:
    """Parse enum to filter."""
    return [get_enum_as_input(enum_value) for enum_value in args]


def get_enum_as_input(enum: str) -> str:
    """Get enum value."""
    return enum.value


def is_list_of_enums(args: List) -> bool:
    """Check list of enums containing."""
    if not args:
        return False
    return isinstance(args[0], Enum)


def is_enum(arg: str) -> bool:
    """Check arg for enum."""
    return isinstance(arg, Enum)


def check_permissions(info, permission_classes):
    """Running all permissions classes in fields."""
    for permission in permission_classes:
        if not permission.has_permissions(info):
            raise PermissionDeniedError()


def decorate_field_resolve(resolve_func, permission_classes):
    """Adding check user permissions before mutate."""

    @wraps(resolve_func)
    def wrapper(root, info, *args, **kwargs):
        check_permissions(info, permission_classes=permission_classes)
        return resolve_func(root, info, *args, **kwargs)

    return wrapper
