from geoluminate.metadata import Metadata

from earth_science.metadata import default_metadata
from earth_science.models.features import SamplingLocation


class GenericSite(SamplingLocation):
    class Meta:
        abstract = False
        verbose_name = "Generic Site"
        verbose_name_plural = "Generic Sites"

    class Config:
        metadata = Metadata(
            **default_metadata,
            primary_data_fields=["char_field"],
            description="A generic site for testing purposes.",
        )
        filterset_fields = ["name", "char_field"]
        # filterset_class = "example.filters.SampleFilter"
        table_class = "example.tables.GenericSiteTable"
