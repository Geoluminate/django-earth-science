from django.utils.translation import gettext as _
from geoluminate.views import BaseDetailView, BaseEditView

from .forms import PointForm
from .models import Point


class PointDetailView(BaseDetailView):
    base_template = "locations/location_detail.html"
    model = Point
    title = _("Point")
    form_class = PointForm
    extra_context = {
        "menu": "LocationDetailMenu",
    }

    def get_object(self, queryset=None):
        return Point.objects.get(x=self.kwargs["lon"], y=self.kwargs["lat"])


class PointEditView(BaseEditView):
    model = Point
    form_class = PointForm
    related_name = "sample"
