from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapp'
    verbose_name = _('blogapp')
