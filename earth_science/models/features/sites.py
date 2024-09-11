from django.utils.translation import gettext as _
from geoluminate.db import models
from geoluminate.db.models import QuantityField
from geoluminate.metadata import Metadata
from geoluminate.models import Sample
from research_vocabs.fields import ConceptField

from earth_science.metadata import default_metadata
from earth_science.vocabularies.odm2 import (
    ElevationDatum,
    SamplingFeatureType,
    SiteType,
)

from ..samples.generic import GenericHole
from ..samples.intervals import GeoDepthInterval


class SamplingLocation(Sample):
    _metadata = Metadata(
        description=_(
            "A sampling location relates to a specific geographic point, defined by precise coordinates (typically latitude and longitude), where samples are collected for scientific analysis. It includes detailed information about the time and date when the location was accessed for sampling, as well as the accessibility conditions, such as terrain, transportation routes, required permits, or any logistical challenges associated with reaching the site. This comprehensive documentation ensures that the sampling efforts are reproducible and that the data collected can be accurately interpreted within the context of its geographical, temporal, and environmental settings."
        ),
        analagous_to=[
            "https://schema.org/Place",
            "https://schema.org/GeoCoordinates",
            SamplingFeatureType().get_concept("site"),
        ],
        **default_metadata,
    )

    type = ConceptField(
        vocabulary=SiteType,
        default="unknown",
        # include_only=settings.get("SAMPLING_LOCATION_TYPES", None),
        verbose_name=_("type"),
        help_text=_("The type of sampling location."),
    )

    location = models.ForeignKey(
        "location.Point",
        verbose_name=_("location"),
        help_text=_("The location of the sample."),
        related_name="samples",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    elevation_datum = ConceptField(
        vocabulary=ElevationDatum,
        default="MSL",
    )
    elevation_method = ConceptField(
        vocabulary=SamplingFeatureType,
        default="site",
        editable=False,
    )
    elevation = QuantityField(
        verbose_name=_("elevation"),
        base_units="m",
        unit_choices=["m", "ft"],
        null=True,
        blank=True,
        help_text=_("Enter the elevation of the site in meters."),
    )

    class Meta:
        abstract = True
        verbose_name = _("sampling location")
        verbose_name_plural = _("sampling locations")

    class Options:
        root_allowed = True
        # description_types = SamplingLocationDescriptions
        # date_types = SamplingLocationDates

    __doc__ = _metadata.description


class Borehole(GeoDepthInterval, GenericHole, SamplingLocation):
    MAX_DEPTH = 12262  # meters
    _metadata = Metadata(
        description=_(
            "A borehole is a narrow, cylindrical shaft drilled into the ground, either vertically or at an angle, to access subsurface materials such as soil, rock, groundwater, or gas for exploration, extraction, or geotechnical investigation purposes. Boreholes are created using drilling equipment and can vary in depth from a few meters to several kilometers, depending on the purpose of the drilling. They are used in a range of applications, including geological and environmental studies, resource exploration (such as oil, gas, and minerals), groundwater monitoring, and engineering assessments for construction projects. Boreholes are characterized by their depth, diameter, orientation, and the specific methods and tools used for drilling and sampling."
        ),
        analagous_to=[
            "https://schema.org/Place",
            "https://schema.org/GeoCoordinates",
            SamplingFeatureType().get_concept("borehole"),
        ],
        **default_metadata,
    )

    def save(self, *args, **kwargs):
        # can't query depth directly because it is a calculated property and is not set until after save
        # if abs(self.bottom - self.top) > self.MAX_DEPTH:
        #     raise ValueError(
        #         _(f"The depth of the borehole exceeds the maximum allowed depth of {self.MAX_DEPTH} meters.")
        #     )
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        verbose_name = _("borehole")
        verbose_name_plural = _("boreholes")
