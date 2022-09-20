from unittest import mock

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from graphql.execution.execute import GraphQLResolveInfo  # type: ignore

UserModel = get_user_model()
request_factory = RequestFactory()


@pytest.fixture()
def authenticated_graphql_info():
    """Authenticated user mock fixture."""
    context = request_factory.post('/')
    context.user = mock.Mock(
        is_authenticated=True,
        spec=UserModel,
    )
    return mock.Mock(
        context=context,
        path=['test'],
        spec=GraphQLResolveInfo,
    )


@pytest.fixture()
def unauthenticated_graphql_info():
    """Anonymous user mock fixture."""
    context = request_factory.post('/')
    context.user = AnonymousUser()
    return mock.Mock(
        context=context,
        path=['test'],
        spec=GraphQLResolveInfo,
    )


@pytest.fixture()
def resolver_func():
    """Empty resolver fixture."""
    def resolver(info, root=None, **kwargs):
        return  # noqa: WPS324
    return resolver
