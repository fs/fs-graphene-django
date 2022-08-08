from graphene import Field

from graphene_django_pretty.fields.utils import decorate_field_resolve


class BaseField(Field):
    """Base graphene field."""

    def __init__(self, *args, permission_classes=None, **kwargs):
        """Init overriding for additional permission classes."""
        self.permission_classes = permission_classes
        super().__init__(*args, **kwargs)

    def wrap_resolve(self, parent_resolver):
        """Wrap resolver."""
        super_wrap = super().wrap_resolve(parent_resolver)
        return decorate_field_resolve(
            super_wrap,
            permission_classes=self.permission_classes or [],
        )
