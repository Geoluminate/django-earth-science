import factory
from factory.django import DjangoModelFactory
from geoluminate.factories import SampleFactory
from geoluminate.factories.generic import RandomM2M
from geoluminate.factories.utils import randint

from earth_science.geology.geologic_time.models import GeologicalTimescale
from earth_science.geology.lithology.models import SimpleLithology
from earth_science.geology.stratigraphy.models import StratigraphicUnit
from earth_science.models.features.sites import Borehole


class PointFactory(DjangoModelFactory):
    x = factory.Faker("pyfloat", min_value=-180, max_value=180)
    y = factory.Faker("pyfloat", min_value=-90, max_value=90)

    samples = factory.RelatedFactoryList(
        "geoluminate.factories.SampleFactory",
        factory_related_name="Point",
        size=randint(2, 8),
    )

    class Meta:
        model = "location.Point"


class SamplingLocationFactory(SampleFactory):
    type = factory.Faker("word")
    location = factory.SubFactory(PointFactory, samples=None)
    elevation = factory.Faker("pyfloat", min_value=-8000, max_value=3500)

    # class Meta:
    # model = "example.GenericSite"


class HoleFactory(SampleFactory):
    azimuth = factory.Faker("pyfloat", min_value=0, max_value=360)
    inclination = factory.Faker("pyfloat", min_value=0, max_value=90)
    length = factory.Faker("pyfloat", min_value=0, max_value=1000)


class VerticalIntervalFactory(SampleFactory):
    top = factory.Faker("pyfloat", min_value=0, max_value=1000)
    bottom = factory.Faker("pyfloat", min_value=0, max_value=1000)


class GeoDepthIntervalFactory(VerticalIntervalFactory):
    class Params:
        max_depth = Borehole.HOLE_MAX_LENGTH

    top = 0
    bottom = factory.Faker("pyfloat", min_value=0, max_value=1000)

    lithology = RandomM2M(SimpleLithology, related_field="lithology", count=3)
    age = RandomM2M(GeologicalTimescale, related_field="age", count=3)
    stratigraphy = RandomM2M(StratigraphicUnit, related_field="stratigraphy", count=3)


class BoreholeFactory(HoleFactory, GeoDepthIntervalFactory, SamplingLocationFactory):
    pass
