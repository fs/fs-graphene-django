import json
from unittest import mock
import pytest
from graphene_django.utils.testing import graphql_query
from graphene.test import Client

from tests.django_setup.schema import schema


@pytest.fixture
def client_query():
    client = Client(schema)

    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func


def test_mutation(client_query):
    response = client_query(
        '''
        mutation {
            mutation(input: {test: "test"}) {
                message
            }
        }
        ''',

    )
    data = json.loads(response.content)
    # assert data['errors'][0]['message'] == "'WSGIRequest' object has no attribute 'user'"


def test_login_required_mutation(client_query):
    client = Client(schema)
    response = client.execute(
        '''
        mutation {
            loginRequired(input: {test: "test"}) {
                message
            }
        }
        ''',

    )
    print(response)
    assert response['errors'][0]['message'] == "'WSGIRequest' object has no attribute 'user'"
