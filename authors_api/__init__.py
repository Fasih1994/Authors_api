from .celery import (
    app as celery_app,  # To make sure celery is present on django startup
)

__all__ = ("celery_app",)
