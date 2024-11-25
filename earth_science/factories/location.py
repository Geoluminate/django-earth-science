import factory
from factory.django import DjangoModelFactory
from geoluminate.factories import SampleFactory
from geoluminate.factories.utils import randint


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
    elevation = factory.Faker("pyfloat", positive=True)

    class Meta:
        model = "example.GenericSite"
