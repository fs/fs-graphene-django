import re
from typing import Union

status_code_pattern = re.compile('^[A-Z]+(?:_[A-Z]+)*$')

StatusCode = Union[str, int]

error_text = (
    'Status code is not valid! Please provide' +
    'status code with underscores and in uppercase style.'
)


class StatusCodeError(ValueError):
    """Custom ValueError for invalid status code."""

    def __init__(self, *args: object) -> None:
        """Overriding with status code text."""
        super().__init__(error_text, *args)


def validate_status_code(code: StatusCode):
    """Validate status code style."""
    if isinstance(code, str) and not status_code_pattern.match(code):
        raise StatusCodeError
