import graphene


class BasePayload(graphene.ObjectType):
    """Base payload for all mutations in project."""

    ok = graphene.Boolean(required=True)
    message = graphene.String(required=True)
    errors = graphene.List(graphene.String, required=True)
    # query = graphene.Field('server.schema.Query', required=True)

    def resolve_message(self, _):
        """Resolving info message."""
        no_errors = self.ok is None and not self.errors
        if not self.message:
            return ('Success' if self.ok or no_errors else 'Fail')

        return self.message

    def resolve_ok(self, _):
        """Resolving OK field."""
        return not self.errors

    def resolve_errors(self, _):
        """Resolving errors."""
        return self.errors or []
