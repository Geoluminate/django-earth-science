from earth_science.tables import PointTable

from .models import GenericSite


class GenericSiteTable(PointTable):
    class Meta:
        model = GenericSite
        exclude = ["site_icon", "path", "has_children", "has_parent"]
        fields = [
            "dataset",
            "id",
            "name",
            "location.crs",
            "latitude",
            "longitude",
        ]
