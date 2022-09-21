from functools import partial, wraps
from typing import Any, Callable, List, Tuple, TypeVar, Union, cast

from django.contrib.auth import get_user_model
from graphql.type.definition import GraphQLResolveInfo

from graphene_django_pretty.auth.exceptions import PermissionDeniedError

User = get_user_model()


FuncT = TypeVar("FuncT", bound=Callable[..., Any])


def find_context(func):
    """Return context from GraphQLResolveInfo in resolvers or mutations."""
    def wrapper(*args, **kwargs):
        info = next(  # noqa: WPS110
            arg
            for arg in args
            if isinstance(arg, GraphQLResolveInfo)
        )
        return func(info.context, *args, **kwargs)

    return wrapper


def user_passes_test(test_func, exc=PermissionDeniedError) -> FuncT:
    """Decorator factory."""
    def decorator(func) -> FuncT:
        @wraps(func)
        @find_context
        def wrapper(context, *args, **kwargs):
            if test_func(context.user):
                return func(*args, **kwargs)
            raise exc()

        return cast(FuncT, wrapper)

    return cast(FuncT, decorator)


def check_perms(user: User, perm: Union[Tuple[str], str]) -> bool:  # type: ignore
    """Check user having permission."""
    if isinstance(perm, str):
        perms = (perm,)
    else:
        perms = perm
    return user.has_perms(perms)  # type: ignore


def permission_required(perm: Union[List[str], str]):
    """Permission required decorator like in django."""
    func = partial(check_perms, perm=perm)
    return user_passes_test(func)


login_required = user_passes_test(lambda user: user.is_authenticated)  # type: ignore
staff_member_required = user_passes_test(lambda user: user.is_staff)  # type: ignore
superuser_required = user_passes_test(lambda user: user.is_superuser)  # type: ignore
