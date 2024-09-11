from django.utils.translation import gettext as _
from geoluminate.db import models
from geoluminate.metadata import Metadata
from geoluminate.models import Sample

from earth_science.vocabularies.odm2 import (
    SamplingFeatureType,
)


class SamplingArea(Sample):
    geom = models.JSONField(
        verbose_name=_("geometry"),
        help_text=_("A geojson formatted polygon representing the sampling area."),
    )

    _metadata = Metadata(
        description=_(
            "A sampling area is a defined geographic region represented by a polygon, encompassing multiple sampling locations within its boundaries, where samples are systematically collected for scientific analysis. This area is delineated based on specific research objectives, environmental characteristics, or spatial patterns of interest, and is described by a set of coordinates that outline its perimeter. The sampling area includes information on its geographic extent, access routes, environmental conditions, and the times and dates of sampling activities. By capturing a range of conditions across a broader geographic context, a sampling area provides a more comprehensive understanding of the variability and distribution of the phenomena being studied."
        ),
        analagous_to=[
            "https://schema.org/Place",
            SamplingFeatureType().get_concept("fieldArea"),
        ],
    )

    class Meta:
        verbose_name = _("sampling area")
        verbose_name_plural = _("sampling areas")

    class Options:
        root_allowed = True

    __doc__ = _metadata.description
