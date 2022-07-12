from typing import Any
import inspect

from django.db import models

from graphene_django_pretty.utils import DJANGO_POLYMORPHIC_INSTALLED


def is_valid_django_model(model: Any) -> bool:
    """Django model class validation."""
    is_django_model = inspect.isclass(model) and issubclass(model, models.Model)

    if DJANGO_POLYMORPHIC_INSTALLED and not is_django_model:
        from polymorphic.models import PolymorphicModel
        return issubclass(model, PolymorphicModel)

    return is_django_model
