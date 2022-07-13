from graphene import Field
from graphene_django_pretty.fields.utils import decorate_field_resolve


class BaseField(Field):
    def __init__(self, *args, permission_classes=None, **kwargs):
        self.permission_classes = permission_classes
        super(BaseField, self).__init__(*args, **kwargs)

    def wrap_resolve(self, parent_resolver):
        super_wrap = super(BaseField, self).wrap_resolve(parent_resolver)
        result = decorate_field_resolve(super_wrap, permission_classes=self.permission_classes or [])
        return result
