from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView
from flex_menu import Menu, MenuItem
from geoluminate.plugins import PluginRegistry

from .models import Point

LocationDetailMenu = Menu(
    "LocationDetailMenu",
    label=_("Location"),
    root_template="geoluminate/menus/detail/root.html",
    children=[
        MenuItem(
            _("Overview"), view_name="location-detail", icon="grid", template="geoluminate/menus/detail/menu.html"
        ),
    ],
)


class LocationPluginRegistry(PluginRegistry):
    menus = {
        "location": LocationDetailMenu,
    }


plugins = LocationPluginRegistry()


def register(to, **kwargs):
    """Decorator to register a page view and add it as an item to the page menu."""

    def decorator(view_class):
        plugins.register(view_class, to, **kwargs)
        return view_class

    return decorator


# LOCATION PLUGINS
@register(["location"])
class PointOverview(UpdateView):
    model = Point
    template_name = "geoluminate/plugins/overview.html"
    icon = "location"
    # base_template = "location/location_detail.html"
    # template_name = "geoluminate/plugins/map.html"
