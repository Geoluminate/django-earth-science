from django.utils.translation import gettext as _
from geoluminate.models import Sample
from research_vocabs.fields import ConceptField

from earth_science.utils import is_abstract
from earth_science.vocabularies.odm2 import Medium, SamplingFeatureType, SpecimenType


class GenericSite(Sample):
    feature_type = ConceptField(
        vocabulary=SamplingFeatureType,
        default="site",
        editable=False,
    )

    medium = None

    specimen_type = None

    class Meta:
        abstract = is_abstract("GenericSite")
        verbose_name = _("site")
        verbose_name_plural = _("sites")


class GenericEarthSample(Sample):
    feature_type = ConceptField(
        vocabulary=SamplingFeatureType,
    )
    medium = ConceptField(
        verbose_name=_("medium"),
        vocabulary=Medium,
        default="solid",
    )
    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="theSpecimenTypeIsUnknown",
    )

    class Meta:
        abstract = is_abstract("GenericEarthSample")
        verbose_name = _("generic earth sample")
        verbose_name_plural = _("generic earth samples")
