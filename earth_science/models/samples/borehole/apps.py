from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BoreholeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "earth_science.samples.borehole"
    verbose_name = _("borehole")
    verbose_name_plural = _("boreholes")
