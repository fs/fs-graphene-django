from graphene_django_pretty.auth.decorators import login_required


class OR:
    """Logic or operator class for permission classes."""

    def __init__(self, op1, op2) -> None:
        """Init OR class by to permission classes."""
        self.op1 = op1
        self.op2 = op2

    def has_permissions(self, info, _):  # noqa: WPS110
        """Permission checking for union."""
        return (
            self.op1.has_permissions(info, _) or
            self.op2.has_permissions(info, _)
        )


class PermissionMeta(type):
    """Permission union metaclass."""

    def __or__(cls, permission) -> OR:
        """Returns instance of or class realization."""
        return OR(cls, permission)


class BasePermission(metaclass=PermissionMeta):
    """Base permissions."""

    @classmethod
    def has_permissions(cls, *args, **kwargs):
        """Permissions check method."""
        raise NotImplementedError('has_permissions not implemented.')


class AuthenticationRequired(BasePermission):
    """Authentication required permission."""

    @classmethod
    @login_required
    def has_permissions(cls, *args, **kwargs):
        """Check permissions in login_required decorator."""
        return True
