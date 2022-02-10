from graphql.error.graphql_error import GraphQLError


class GrapheneDjangoError(GraphQLError):
    """Base abstract exception."""

    default_message = None

    def __init__(self, message=None, *args, **kwargs):
        if not message:
            message = self.default_message
        super().__init__(message=message, *args, **kwargs)
