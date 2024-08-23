from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LocationConfig(AppConfig):
    name = "earth_science.location"
    label = "location"
    verbose_name = _("Location")

    def ready(self) -> None:
        from actstream import registry

        registry.register(self.get_model("Point"))

        return super().ready()
