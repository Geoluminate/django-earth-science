from django.utils.translation import gettext as _
from geoluminate.contrib.samples.models import Sample
from geoluminate.db import models
from quantityfield.fields import QuantityField
from research_vocabs.fields import ConceptField

from earth_science.vocabularies.cgi.geosciml import SimpleLithology
from earth_science.vocabularies.stratigraphy import ISC2020


class Borehole(Sample):
    # depth_top
    # depth_bottom
    # total_depth
    # vertical_datum

    # azimuth
    # inclination

    class Meta:
        verbose_name = _("borehole")
        verbose_name_plural = _("boreholes")


class DepthInterval(Sample):
    parent = models.ForeignKey(
        Borehole,
        verbose_name=_("parent"),
        help_text=_("The parent heat flow site."),
        on_delete=models.CASCADE,
    )

    lithology = ConceptField(
        vocabulary=SimpleLithology,
        null=True,
        blank=True,
    )

    stratigraphy = ConceptField(
        vocabulary=ISC2020,
        help_text=_(
            "Stratigraphic age of the depth range involved in the reported heat-flow determination based on the"
            " official geologic timescale of the International Commission on Stratigraphy."
        ),
        blank=True,
        null=True,
    )

    depth_top = QuantityField(
        base_units="m",
        verbose_name=_("interval top"),
        help_text=_(
            "Describes the true vertical depth (TVD) of the top end of the heat-flow determination interval relative to"
            " the land surface/seafloor."
        ),
        blank=True,
        null=True,
    )

    depth_bottom = QuantityField(
        base_units="m",
        verbose_name=_("interval bottom"),
        help_text=_(
            "Describes the true vertical depth (TVD) of the bottom end of the heat-flow determination interval relative"
            " to the land surface."
        ),
        blank=True,
        null=True,
    )

    total_depth = QuantityField(
        base_units="m",
        verbose_name=_("total depth"),
        help_text=_("Describes the total depth of the borehole."),
        blank=True,
        null=True,
    )

    # depth_top
    # depth_bottom
    # vertical_datum
    # total_depth

    # azimuth
    # inclination

    class Meta:
        verbose_name = _("depth interval")
        verbose_name_plural = _("depth intervals")
