from enum import Enum
from typing import List


def get_enum_list_as_input(args: List) -> List[str]:
    """Parse enum to filter."""
    return [get_enum_as_input(enum_value) for enum_value in args]


def get_enum_as_input(enum: str) -> str:
    """Get enum value."""
    return enum.value


def is_list_of_enums(args: List) -> bool:
    """Check list of enums containing."""
    if not args:
        return False
    return isinstance(args[0], Enum)


def is_enum(arg: str) -> bool:
    """Check arg for enum."""
    return isinstance(arg, Enum)
