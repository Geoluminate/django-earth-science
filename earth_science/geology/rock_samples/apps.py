from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RockSamplesConfig(AppConfig):
    name = "earth_science.geology.rock_samples"
    label = "rock_samples"
    verbose_name = _("Rock Sample")
    verbose_name = _("Rock Samples")
