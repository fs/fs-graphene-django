from fs_graphene_django.error.format import format_error
from graphene_django.views import GraphQLView


class PrettyGraphQLView(GraphQLView):

    @staticmethod
    def format_error(error):
        if isinstance(error, GraphQLError):
            return format_error(error)

        return {"message": str(error)}
