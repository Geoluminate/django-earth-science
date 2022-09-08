from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class EarthScienceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'earth_science'
    verbose_name = _('Earth Science')
