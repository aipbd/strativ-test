import factory
from factory.django import DjangoModelFactory

from strativ_test.apps.countries.models import Country


class CountryFactory(DjangoModelFactory):
    name = factory.Faker("word")
    alpha_code2 = factory.Faker("word")
    alpha_code3 = factory.Faker("word")

    class Meta:
        model = Country
