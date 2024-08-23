from django.utils.translation import gettext as _
from geoluminate.views import BaseDetailView, BaseEditView

from .forms import PointForm
from .models import Point


class PointDetailView(BaseDetailView):
    base_template = "location/location_detail.html"
    model = Point
    title = _("Point")
    form_class = PointForm


class PointEditView(BaseEditView):
    model = Point
    form_class = PointForm
    related_name = "sample"
