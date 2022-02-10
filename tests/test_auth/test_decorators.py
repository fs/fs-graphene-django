import pytest

from graphene_django_pretty.auth.exceptions import PermissionDeniedError
from graphene_django_pretty.auth.decorators import login_required


def test_authenticated_login_required(authenticated_graphql_info, resolver_func):
    func = login_required(resolver_func)
    func(info=authenticated_graphql_info)


def test_unauthenticated_login_required(unauthenticated_graphql_info, resolver_func):
    func = login_required(resolver_func)
    with pytest.raises(PermissionDeniedError):
        func(info=unauthenticated_graphql_info)

