from graphene_django.views import GraphQLView
from graphql import GraphQLError

from graphene_django_pretty.error.format import format_error


class PrettyGraphQLView(GraphQLView):
    """GraphQL view with error formatting."""

    @staticmethod
    def format_error(error):  # noqa: D102
        if isinstance(error, GraphQLError):
            return format_error(error)

        return {'message': str(error)}
