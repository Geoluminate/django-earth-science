import factory
from geoluminate.factories.utils import randint

from earth_science.location.models import Point


class PointFactory(factory.django.DjangoModelFactory):
    x = factory.Faker("pyfloat", min_value=-180, max_value=180)
    y = factory.Faker("pyfloat", min_value=-90, max_value=90)

    samples = factory.RelatedFactoryList(
        "geoluminate.factories.SampleFactory",
        factory_related_name="Point",
        size=randint(2, 8),
    )

    class Meta:
        model = Point
