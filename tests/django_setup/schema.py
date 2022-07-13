import graphene
from graphene_django_pretty.auth.permissions import AuthenticationRequired
from graphene_django_pretty.fields.base import BaseField
from graphene_django_pretty.mutations.base import BaseMutation
from graphene_django_pretty.mutations.output import BasePayload
from graphene_django_pretty.scalars.email import Email


class Query(graphene.ObjectType):

    test = BaseField(graphene.String)
    login_required_test = BaseField(graphene.String, permission_classes=[AuthenticationRequired])

    @classmethod
    def resolve_test(cls, root, info):
        return "OK"

    @classmethod
    def resolve_login_required_test(cls, root, info):
        return "OK"


class TestInput(graphene.InputObjectType):

    test = graphene.String()


class EmailInput(graphene.InputObjectType):

    email = Email()


class EmailMutation(BaseMutation):
    Input = EmailInput()
    Output = BasePayload

    @classmethod
    def mutate(cls, info, *args, **kwargs):
        return cls.Output(message='OK')


class Mutation(BaseMutation):

    Input = TestInput()
    Output = BasePayload

    @classmethod
    def mutate(cls, info, *args, **kwargs):
        return cls.Output(message='OK')


class LoginRequiredMutation(Mutation):
    permission_classes = [AuthenticationRequired]


class Mutations(graphene.ObjectType):
    mutation = Mutation.Field()
    login_required = LoginRequiredMutation.Field()
    email = EmailMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
