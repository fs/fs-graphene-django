from graphene import ObjectType
from graphene.types.base import BaseOptions
from graphene.types.utils import yank_fields_from_attrs


class DjangoObjectOptions(BaseOptions):
    fields = None
    input_fields = None
    interfaces = ()
    model = None
    queryset = None
    registry = None
    connection = None
    create_container = None
    results_field_name = None
    filter_fields = ()
    input_for = None
    filterset_class = None


class DjangoObjectType(ObjectType):
    @classmethod
    def __init_subclass_with_meta__(
        cls,
        model=None,
        registry=None,
        skip_registry=False,
        only_fields=(),
        exclude_fields=(),
        include_fields=(),
        filter_fields=None,
        interfaces=(),
        filterset_class=None,
        **options,
    ):
        assert is_valid_django_model(model), (
            'You need to pass a valid Django Model in {}.Meta, received "{}".'
        ).format(cls.__name__, model)

        if not registry:
            registry = get_global_registry()

        assert isinstance(registry, Registry), (
            "The attribute registry in {} needs to be an instance of "
            'Registry, received "{}".'
        ).format(cls.__name__, registry)

        if not DJANGO_FILTER_INSTALLED and (filter_fields or filterset_class):
            raise Exception(
                "Can only set filter_fields or filterset_class if Django-Filter is installed"
            )

        django_fields = yank_fields_from_attrs(
            construct_fields(
                model, registry, only_fields, include_fields, exclude_fields
            ),
            _as=Field,
        )

        _meta = DjangoObjectOptions(cls)
        _meta.model = model
        _meta.registry = registry
        _meta.filter_fields = filter_fields
        _meta.fields = django_fields
        _meta.filterset_class = filterset_class

        super(DjangoObjectType, cls).__init_subclass_with_meta__(
            _meta=_meta, interfaces=interfaces, **options
        )

        if not skip_registry:
            registry.register(cls)

    def resolve_id(self, info):
        return self.pk

    @classmethod
    def is_type_of(cls, root, info):
        if isinstance(root, SimpleLazyObject):
            root._setup()
            root = root._wrapped
        if isinstance(root, cls):
            return True
        if not is_valid_django_model(type(root)):
            raise Exception(('Received incompatible instance "{}".').format(root))
        return isinstance(root, cls._meta.model)

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset

    @classmethod
    def get_node(cls, info, id):
        try:
            return cls._meta.model.objects.get(pk=id)
        except cls._meta.model.DoesNotExist:
            return None
