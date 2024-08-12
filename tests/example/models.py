from geoluminate.db import models
from geoluminate.models import Measurement, Sample


class CustomParentSample(Sample):
    # standard django fields
    char_field = models.CharField(
        "Character Field", max_length=200, help_text="Enter a string of up to 200 characters."
    )

    class Meta:
        verbose_name = "Parent Sample"
        verbose_name_plural = "Parent Samples"


class CustomSample(Sample):
    # standard django fields
    char_field = models.CharField(
        "Character Field", max_length=200, help_text="Enter a string of up to 200 characters."
    )

    class Meta:
        verbose_name = "Child Sample"
        verbose_name_plural = "Child Samples"


class ExampleMeasurement(Measurement):
    float_field = models.FloatField("Float Field", help_text="Enter a floating point number.")
