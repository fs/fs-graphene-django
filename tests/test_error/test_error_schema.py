import pytest

from graphene_django_pretty.error.exceptions import BaseGraphQLError
from tests.django_setup.errors import DefaultError


class GraphQLTestError(BaseGraphQLError):
    """Error class with defaults for test."""

    default_code: int = 404
    default_message: str = 'test default'


@pytest.mark.parametrize(
    'error',
    [
        None,
        BaseGraphQLError(code=500, message='test error'),
        BaseGraphQLError(message='test error'),
        BaseGraphQLError(code=500),
        BaseGraphQLError(code='ERROR_CODE', message='test error'),
        GraphQLTestError(),
    ])
def test_errors(error, mock_error, client_query):
    if error:
        mock_error(error)
    else:
        error = DefaultError()
    response: dict[str, list[dict]] = client_query(
        """
            mutation {
                errors(input: {test: "test"}) {
                    message
                }
            }
        """,
    )
    response_error = response['errors'][0]
    if error.message:
        assert response_error['message'] == error.message
    else:
        assert response_error['message'] == 'An unknown error occurred.'
    if error.code:
        assert response_error['extensions']['code'] == error.code
    else:
        with pytest.raises(AttributeError):
            response_error.extensions  # noqa: WPS428
