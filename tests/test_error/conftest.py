import pytest

from graphene_django_pretty.error.exceptions import BaseGraphQLError
from tests.django_setup.errors import errors_dict


@pytest.fixture()
def mock_error(monkeypatch):
    """Mock mutations errors."""
    def func(error: BaseGraphQLError):
        return monkeypatch.setitem(errors_dict, 'error', error)
    return func
