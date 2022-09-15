import re

import graphene
from graphql import GraphQLError, StringValueNode, print_ast


class Email(graphene.Scalar):
    """Email field."""

    serialize = graphene.String.coerce_string
    parse_value = graphene.String.coerce_string

    @classmethod
    def parse_literal(cls, node: StringValueNode, _variables=None):
        """Return validated email field value."""
        pat = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$'
        if not isinstance(node, StringValueNode):
            raise GraphQLError(
                'Email cannot represent non-string value: {0}'.format(
                    print_ast(node),
                ),
            )
        if not re.match(pat, node.value):
            raise GraphQLError('Invalid email address.', nodes=[node])
        return node.value
