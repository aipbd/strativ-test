import requests
from django.core.management.base import BaseCommand

from strativ_test.apps.countries.constants import COUNTRY_GET_URL
from strativ_test.apps.countries.models import Country


def add_countries():
    response = requests.get(COUNTRY_GET_URL)

    if Country.objects.count():
        # Country list already added
        return 0

    if not (response.status_code == 200):
        # raise NotFound
        return 0

    response_json = response.json()
    countries = [
        Country(**{
            "name": country.get("name"),
            "alpha_code2": country.get("alpha2Code"),
            "alpha_code3": country.get("alpha3Code"),
            "capital": country.get("capital"),
            "population": country.get("population"),
            "neighbouring_countries": country.get("borders"),
            "timezones": country.get("timezones"),
            "flag": country.get("flag"),
            "languages": [language.get("name") for language in country.get("languages")],
        })

        for country in response_json
    ]

    added_countries = Country.objects.bulk_create(countries)
    return len(added_countries)


class Command(BaseCommand):

    def handle(self, *args, **options):
        no_of_countries = add_countries()
        print(f"{no_of_countries} countries added.")
