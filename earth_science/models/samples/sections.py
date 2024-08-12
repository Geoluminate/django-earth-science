from django.utils.translation import gettext as _
from research_vocabs.fields import ConceptField

from earth_science.utils import is_abstract
from earth_science.vocabularies.odm2 import Medium, SamplingFeatureType, SpecimenType

from .generic import GenericEarthSample


class Interval(GenericEarthSample):
    feature_type = ConceptField(
        vocabulary=SamplingFeatureType,
        default="interval",
        editable=False,
    )
    medium = ConceptField(
        verbose_name=_("medium"),
        vocabulary=Medium,
        default="rock",
        editable=False,
    )

    class Meta:
        abstract = is_abstract("Interval")
        verbose_name = _("interval")
        verbose_name_plural = _("intervals")


class DepthInterval(Interval):
    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="depthInterval",
        editable=False,
    )

    class Meta:
        abstract = is_abstract("DepthInterval")
        verbose_name = _("depth interval")
        verbose_name_plural = _("depth intervals")


class BoreholeDepthInterval(DepthInterval):
    # also contains fields for borehole length, and other borehole-specific information

    class Meta:
        abstract = is_abstract("BoreholeDepthInterval")
        verbose_name = _("borehole depth interval")
        verbose_name_plural = _("borehole depth intervals")
