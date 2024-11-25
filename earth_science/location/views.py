from django.utils.translation import gettext as _
from geoluminate.views import BaseCRUDView

from .forms import PointForm
from .models import Point
from .plugins import LocationDetailMenu


class PointCRUDView(BaseCRUDView):
    base_template = "locations/location_detail.html"
    model = Point
    title = _("Point")
    form_class = PointForm
    menu = LocationDetailMenu
    paginate_by = 50
    # filterset_class = DatasetFilter
    # sidebar_fields = {
    #     None: ["name", "project", "created", "modified"],
    # }

    def get_object(self, queryset=None):
        return Point.objects.get(x=self.kwargs["lon"], y=self.kwargs["lat"])
