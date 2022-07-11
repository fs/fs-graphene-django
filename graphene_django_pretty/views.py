from graphene_django.views import GraphQLView
from graphene_django_pretty.error.format import format_error
from graphql import GraphQLError


class PrettyGraphQLView(GraphQLView):

    @staticmethod
    def format_error(error):
        if isinstance(error, GraphQLError):
            return format_error(error)

        return {"message": str(error)}
