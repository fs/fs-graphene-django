import re
import graphene
from graphql import StringValueNode, GraphQLError, print_ast


class Email(graphene.Scalar):

    serialize = graphene.String.coerce_string
    parse_value = graphene.String.coerce_string

    @classmethod
    def parse_literal(cls, node, _variables=None):
        pat = r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if not isinstance(node, StringValueNode):
            raise GraphQLError(
                f"DateTime cannot represent non-string value: {print_ast(node)}"
            )
        if not re.match(pat, node.value):
            raise GraphQLError('Invalid email address.', nodes=[node])
        return node.value
