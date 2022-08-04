import pytest

from graphene_django_pretty.error.exceptions import BaseGraphQLError
from graphene_django_pretty.error.types import StatusCodeError


@pytest.mark.parametrize(
    ('code', 'message'),
    [
        (500, 'test error'),
        (None, 'test error'),
        (500, None),
        ('ERROR_CODE', 'test error'),
    ],
)
def test_valid_errors(code, message):
    error = BaseGraphQLError(code=code, message=message)
    assert error.message == message
    assert error.code == code
    if code:
        assert error.extensions == {'code': code}


def test_invalid_error():
    with pytest.raises(StatusCodeError):
        BaseGraphQLError(code='invalid code')
