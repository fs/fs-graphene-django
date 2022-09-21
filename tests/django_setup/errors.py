from graphene_django_pretty.error.exceptions import BaseGraphQLError


class DefaultError(BaseGraphQLError):
    """Test error with default params."""

    default_code: int = 400
    default_message: str = 'Error message'


errors_dict = {
    'error': DefaultError,
}


def error_func() -> BaseGraphQLError:
    """Test func for error rising."""
    raise errors_dict['error']
