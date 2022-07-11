import graphene
from graphene_django_pretty.auth.permissions import AuthenticationRequired
from graphene_django_pretty.mutations.base import BaseMutation
from graphene_django_pretty.mutations.output import BasePayload


class Query(graphene.ObjectType):

    test = graphene.String()

    @classmethod
    def resolve_test(cls, root, info):
        return "test"


class TestInput(graphene.InputObjectType):

    test = graphene.String()


class Mutation(BaseMutation):

    Input = TestInput()
    Output = BasePayload

    @classmethod
    def mutate(cls, info, *args, **kwargs):
        return BasePayload(message='OK')


class LoginRequiredMutation(Mutation):
    permission_classes = [AuthenticationRequired]


class Mutations(graphene.ObjectType):
    mutation = Mutation.Field()
    login_required = LoginRequiredMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
