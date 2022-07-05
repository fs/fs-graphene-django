import inspect
from itertools import chain
from typing import Any

from django.db import models

from graphene_django_pretty.utils import DJANGO_POLYMORPHIC_INSTALLED


def is_valid_django_model(model: Any) -> bool:
    """Django model class validation."""
    is_django_model = inspect.isclass(model) and issubclass(model, models.Model)

    if DJANGO_POLYMORPHIC_INSTALLED and not is_django_model:
        from polymorphic.models import PolymorphicModel
        return issubclass(model, PolymorphicModel)

    return is_django_model


def merge_querysets(*querysets, **kwargs):
    """Merge querysets function."""
    sort_key = kwargs['sort_key']
    reverse_needed = kwargs['reverse']
    queryset = list(chain(*querysets))
    if sort_key:
        reverse = reverse_needed if reverse_needed else False
        queryset.sort(key=lambda qs_item: getattr(
            qs_item, sort_key), reverse=reverse)

    return queryset
