import graphene

from graphene_django_pretty.auth.permissions import AuthenticationRequired
from graphene_django_pretty.fields.base import BaseField
from graphene_django_pretty.mutations.base import BaseMutation
from graphene_django_pretty.mutations.output import BasePayload
from graphene_django_pretty.scalars.email import Email
from tests.django_setup.errors import error_func


class Query(graphene.ObjectType):
    """Schema queries."""

    test = BaseField(graphene.String)
    login_required_test = BaseField(
        graphene.String,
        permission_classes=[AuthenticationRequired],
    )

    @classmethod
    def resolve_test(cls, root, info):
        """Resolver for test field."""
        return 'OK'

    @classmethod
    def resolve_login_required_test(cls, root, info):
        """Resolver for login_required_test field."""
        return 'OK'


class TestInput(graphene.InputObjectType):
    """Input with string field."""

    test = graphene.String()


class EmailInput(graphene.InputObjectType):
    """Input with email field."""

    email = Email()


class EmailMutation(BaseMutation):
    """Mutation with email input."""

    Input = EmailInput()
    Output = BasePayload

    @classmethod
    def mutate(cls, info, *args, **kwargs):
        """Mutate field."""
        return cls.Output(message='OK')


class Mutation(BaseMutation):
    """Mutation for simpel string field."""

    Input = TestInput()
    Output = BasePayload

    @classmethod
    def mutate(cls, info, *args, **kwargs):
        """Mutate field."""
        return cls.Output(message='OK')


class LoginRequiredMutation(Mutation):
    """Mutation with auth permission."""

    permission_classes = [AuthenticationRequired]


class ErrorMutation(Mutation):
    """Mutation with error rising."""

    @classmethod
    def mutate(cls, info, *args, **kwargs):
        """Mutate field."""
        return error_func()


class Mutations(graphene.ObjectType):
    """Schema mutations."""

    mutation = Mutation.Field()
    login_required = LoginRequiredMutation.Field()
    email = EmailMutation.Field()
    errors = ErrorMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
