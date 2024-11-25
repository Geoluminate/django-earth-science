import django_tables2 as tables
from django.utils.translation import gettext_lazy as _
from easy_icons import icon
from geoluminate.contrib.core.tables import SampleTable


class PointTable(SampleTable):
    latitude = tables.Column(accessor="location.x", verbose_name=_("Latitude"))
    longitude = tables.Column(accessor="location.y", verbose_name=_("Longitude"))
    site_icon = tables.Column(accessor="location", linkify=True)

    def render_site_icon(self, record):
        return icon("location")
