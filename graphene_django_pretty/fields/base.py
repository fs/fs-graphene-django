from graphene import Field

from graphene_django_pretty.fields.utils import decorate_field_resolve


class BaseField(Field):
    """Base graphene field."""

    def __init__(self, *args, permission_classes=None, **kwargs) -> None:
        """Init overriding for additional permission classes."""
        self.permission_classes = permission_classes
        super(BaseField, self).__init__(*args, **kwargs)  # noqa: WPS608

    def wrap_resolve(self, parent_resolver):
        """Wraps a function resolver with permission classes."""
        super_wrap = super(BaseField, self).wrap_resolve(parent_resolver)  # noqa: E501, WPS608
        return decorate_field_resolve(  # type: ignore
            super_wrap, permission_classes=self.permission_classes or [],
        )
