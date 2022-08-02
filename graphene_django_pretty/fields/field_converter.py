import graphene
from django import forms
from graphene_django.forms.converter import convert_form_field


@convert_form_field.register(forms.MultipleChoiceField)
def convert_form_field_to_enum_list(field):
    """Overriding graphene_django django_filters field with choices converting."""
    enum = graphene.Enum(field.label, field.choices)
    return graphene.List(enum, required=field.required)


@convert_form_field.register(forms.ChoiceField)
def convert_form_field_to_enum(field):
    """Overriding graphene_django django_filters field with choices converting."""
    enum = graphene.Enum(field.label, list(field.choices)[1:])
    # [1:] need for exclude first invalid choice.
    # ChoiceField generates ('', '---------') as a first element.
    return enum(required=field.required)
