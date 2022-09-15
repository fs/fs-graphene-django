try:  # noqa: WPS229
    import django_filters  # noqa: F401, WPS433

    DJANGO_FILTER_INSTALLED = True
except ImportError:
    DJANGO_FILTER_INSTALLED = False


try:  # noqa: WPS229
    import polymorphic  # noqa: F401, WPS433

    DJANGO_POLYMORPHIC_INSTALLED = True
except ImportError:
    DJANGO_POLYMORPHIC_INSTALLED = False
