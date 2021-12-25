import pytest
from django.urls import reverse
from rest_framework import status

from strativ_test.apps.countries.tests.factories import CountryFactory


class BaseCountry:
    @pytest.fixture
    def country(self):
        return CountryFactory()


class TestCountryListAPI(BaseCountry):

    url = reverse("api:countries:country_list")

    def test_unauthorized_country_list(self, country, client):
        response = client.get(self.url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_country_list(self, country, auth_client):
        response = auth_client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data

    def test_country_search(self, country, auth_client):
        country_2 = CountryFactory()
        search_url = f"{self.url}?name={country_2.name}"

        response = auth_client.get(search_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1


class TestCountryDetailsAPI(BaseCountry):
    @pytest.fixture
    def url(self, country):
        return reverse(
            "api:countries:country_detail",
            kwargs={"pk": country.id},
        )

    def test_unauthorized_country_details(self, country, client, url):
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_country_details(self, country, auth_client, url):
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data.get("name") == country.name

    def test_country_details_with_neighbouring_countries(self, country, auth_client, url):
        neighbouring_country_1 = country
        neighbouring_country_2 = CountryFactory(neighbouring_countries=neighbouring_country_1.alpha_code2)

        neighbouring_country_1.neighbouring_countries = [neighbouring_country_2.alpha_code2]
        neighbouring_country_1.save()

        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert neighbouring_country_2.alpha_code2 in response.data.get("neighbouring_countries")
