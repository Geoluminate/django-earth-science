from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView
from flex_menu import Menu
from geoluminate.plugins import PluginRegistry

from .models import Point
from .views import PointDetailView

LocationDetailMenu = Menu(
    "LocationDetailMenu",
    label=_("Location"),
    root_template="geoluminate/menus/detail/root.html",
)


location = PluginRegistry(base=PointDetailView, menu=LocationDetailMenu)


# LOCATION PLUGINS
@location.page("overview", icon="overview")
class PointOverview(UpdateView):
    model = Point
    template_name = "geoluminate/plugins/overview.html"
    # base_template = "location/location_detail.html"
    # template_name = "geoluminate/plugins/map.html"
