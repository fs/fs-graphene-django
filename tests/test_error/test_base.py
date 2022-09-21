import pytest

from graphene_django_pretty.error.exceptions import BaseGraphQLError
from graphene_django_pretty.error.types import StatusCodeError


@pytest.mark.parametrize(  # noqa: WPS317
    (
        'code',
        'message',
    ),
    [
        (500, 'test error'),
        (None, 'test error'),
        (500, None),
        ('ERROR_CODE', 'test error'),
    ],
)
def test_valid_error_codes(code, message):
    error = BaseGraphQLError(code=code, message=message)
    assert error.message == message or BaseGraphQLError.default_message
    assert error.code == code or BaseGraphQLError.default_code
    if code:
        assert error.extensions == {'code': code}


def test_invalid_error_code():
    with pytest.raises(StatusCodeError):
        BaseGraphQLError(code='invalid code')
