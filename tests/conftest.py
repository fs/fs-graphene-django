
from typing import Iterator

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from graphene.test import Client
from graphene_django.settings import import_from_string

from tests.django_setup.schema import schema

User = get_user_model()


def initial_middleware() -> Iterator[object]:
    """Initial middleware generator."""
    middlewares = settings.GRAPHENE['MIDDLEWARE']
    for middleware in middlewares:
        middleware_class = import_from_string(middleware, 'MIDDLEWARE')
        yield middleware_class()


@pytest.fixture()
def request_factory():
    """Request factory fixture."""
    return RequestFactory()


@pytest.fixture()
def client_query(request_factory):
    """GraphQL request factory."""  # noqa: D403
    client = Client(schema, middleware=list(initial_middleware()))

    def func(query, user=None, **query_params):
        request = request_factory.post(
            '/', USER_ID=(user.id if user else None),
        )
        query_params.update(context=request)
        return client.execute(query, **query_params)

    return func


@pytest.fixture()
def user_fixture():
    """Test user fixture."""
    return User.objects.create_user(username='test', password='test')
