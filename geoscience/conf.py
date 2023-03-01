"""Settings for Django CrossRef."""
from appconf import AppConf
from django.conf import settings

__all__ = ("settings", "EarthScienceConf")

class EarthScienceConf(AppConf):
    """Settings for Django Earth Science"""

    INCLUDE = []

    class Meta:
        """Prefix for all Django Earth Science settings."""
        prefix = "EARTHSCIENCE"