import graphene
from graphene.utils import get_unbound_function, props
from graphene_django_pretty.mutations.utils import decorate_mutate_func


class BaseMutation(graphene.Mutation):
    """Base mutation with extra functions."""
    permission_classes = None

    @classmethod
    def setup_input_class(cls, input_class):
        """Added extra attrs for input class."""
        kwargs = input_class.kwargs
        if 'required' not in kwargs:
            kwargs.update({'required': True})

    @classmethod
    def __init_subclass_with_meta__(  # noqa: WPS211
        cls,
        interfaces=(),
        resolver=None,
        output=None,
        arguments=None,
        _meta=None,
        **options,
    ):
        """Change functions."""
        if not arguments:
            input_class = getattr(cls, 'Input', None)

            if input_class:
                cls.setup_input_class(input_class)
                input_class = type('Arguments', (), {'input': input_class})
                arguments = props.props(input_class)
            else:
                arguments = {}

        if not resolver:
            mutate = getattr(cls, 'mutate', None)
            mutate = decorate_mutate_func(mutate, cls.permission_classes or [])
            resolver = get_unbound_function.get_unbound_function(mutate)

        super().__init_subclass_with_meta__(
            resolver=resolver, output=output, arguments=arguments, _meta=_meta, **options,
        )

    @classmethod
    def mutate(cls, info, **kwargs):
        """Abstract method."""
        raise NotImplementedError('mutate() is not implemented for {0}'.format(cls.__name__))
