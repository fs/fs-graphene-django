from fs_graphene_django.types.base import BaseDjangoObjectType


class PolymorphicObjectType(BaseDjangoObjectType):
    """Customization for polymorphic type."""

    class Meta:
        abstract = True

    @classmethod
    def is_type_of(cls, root, info):
        """Check model equality."""
        if cls._meta.model._meta.proxy:
            model = root._meta.model
        else:
            model = root._meta.model._meta.concrete_model

        is_direct_instance = super().is_type_of(root, info)

        return is_direct_instance or issubclass(model, cls._meta.model)
